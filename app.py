from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from pydantic import BaseModel
from typing import Optional, List
import asyncio
import time

# 初始化应用
app = FastAPI(
    title="FastAPI 案例 Demo",
    description="一个包含多种功能的 FastAPI 示例应用",
    version="1.0.0"
)

# 添加 CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 密码加密配置
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT 配置
SECRET_KEY = "your-secret-key-change-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# 安全认证方案
security = HTTPBearer()

# 数据模型
class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None

class Item(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
    count: int = 0

class Message(BaseModel):
    message: str

# 模拟数据存储
fake_users_db = {
    "admin": {
        "username": "admin",
        "email": "admin@example.com",
        "full_name": "Admin User",
        "hashed_password": pwd_context.hash("password123")
    },
    "user1": {
        "username": "user1",
        "email": "user1@example.com",
        "full_name": "Normal User",
        "hashed_password": pwd_context.hash("mypassword")
    }
}

fake_items_db = [
    Item(name="苹果", price=3.99, description="新鲜的红苹果", count=10),
    Item(name="香蕉", price=2.49, description="成熟的黄香蕉", count=15),
    Item(name="橙子", price=4.99, description="甜美的橙子", count=8)
]

# 工具函数
def verify_password(plain_password, hashed_password):
    """验证密码"""
    return pwd_context.verify(plain_password, hashed_password)

def get_user(username: str):
    """根据用户名获取用户"""
    if username in fake_users_db:
        user_data = fake_users_db[username].copy()
        return user_data
    return None

def authenticate_user(username: str, password: str):
    """验证用户凭据"""
    user = get_user(username)
    if not user or not verify_password(password, user["hashed_password"]):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """创建访问令牌"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_token(token: str):
    """解码 JWT 令牌"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="无法解析用户名")
        return username
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="无效的令牌")

# 路由定义

# 主页
@app.get("/", response_model=Message)
async def read_root():
    """欢迎页面"""
    return {"message": "欢迎来到 FastAPI 案例 Demo!"}

# 用户注册
@app.post("/register", response_model=Token, summary="用户注册")
async def register(user: User, password: str):
    """注册新用户"""
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="用户名已存在")
    
    hashed_password = pwd_context.hash(password)
    fake_users_db[user.username] = {
        "username": user.username,
        "email": user.email,
        "full_name": user.full_name,
        "hashed_password": hashed_password
    }
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

# 用户登录
@app.post("/login", response_model=Token, summary="用户登录")
async def login(user_credentials: UserLogin):
    """用户登录接口"""
    user = authenticate_user(user_credentials.username, user_credentials.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="用户名或密码错误",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user_credentials.username}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

# 获取当前用户信息
@app.get("/users/me", response_model=User, summary="获取当前用户信息")
async def read_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """获取当前认证用户的信息"""
    username = decode_token(credentials.credentials)
    user = get_user(username)
    if user is None:
        raise HTTPException(status_code=401, detail="用户不存在")
    
    return User(
        username=user["username"],
        email=user.get("email"),
        full_name=user.get("full_name")
    )

# 获取用户列表（需要认证）
@app.get("/users", response_model=List[User], summary="获取用户列表")
async def read_users(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """获取所有用户列表"""
    decode_token(credentials.credentials)  # 验证令牌
    
    users_list = []
    for username, user_data in fake_users_db.items():
        users_list.append(User(
            username=user_data["username"],
            email=user_data.get("email"),
            full_name=user_data.get("full_name")
        ))
    
    return users_list

# 商品相关路由
@app.get("/items", response_model=List[Item], summary="获取商品列表")
async def read_items(skip: int = 0, limit: int = 100):
    """获取商品列表，支持分页"""
    return fake_items_db[skip : skip + limit]

@app.get("/items/{item_id}", response_model=Item, summary="获取特定商品")
async def read_item(item_id: int):
    """根据 ID 获取特定商品"""
    if item_id < 0 or item_id >= len(fake_items_db):
        raise HTTPException(status_code=404, detail="商品未找到")
    return fake_items_db[item_id]

@app.post("/items", response_model=Item, summary="添加商品")
async def create_item(item: Item, credentials: HTTPAuthorizationCredentials = Depends(security)):
    """添加新商品（需要认证）"""
    decode_token(credentials.credentials)  # 验证令牌
    fake_items_db.append(item)
    return item

# 异步任务示例
@app.post("/send-email", summary="发送邮件（异步任务）")
async def send_email(background_tasks: BackgroundTasks, email: str, message: str):
    """模拟发送邮件的后台任务"""
    
    def send_email_task(email: str, message: str):
        # 模拟发送邮件过程
        print(f"正在发送邮件到 {email}: {message}")
        time.sleep(2)  # 模拟耗时操作
        print(f"邮件已发送到 {email}")
    
    background_tasks.add_task(send_email_task, email, message)
    return {"message": "邮件发送任务已添加到后台"}

# 受保护的路由示例
@app.get("/protected", summary="受保护的路由")
async def protected_route(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """需要认证才能访问的路由"""
    username = decode_token(credentials.credentials)
    return {"message": f"你好, {username}! 这是一个受保护的路由"}

# 错误处理示例
@app.get("/error", summary="触发错误示例")
async def trigger_error():
    """演示错误处理"""
    raise HTTPException(status_code=418, detail="这是一个茶壶错误示例")

# 健康检查
@app.get("/health", summary="健康检查")
async def health_check():
    """API 健康检查"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)