from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from pydantic import BaseModel
from typing import Optional

# 初始化应用
app = FastAPI(title="User Authentication API", version="1.0.0")

# 密码加密配置
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT 配置
SECRET_KEY = "your-secret-key-change-in-production"  # 生产环境中应从环境变量获取
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

# 模拟用户数据库
fake_users_db = {
    "admin": {
        "username": "admin",
        "hashed_password": pwd_context.hash("password123")  # 密码是 "password123"
    },
    "user1": {
        "username": "user1",
        "hashed_password": pwd_context.hash("mypassword")
    }
}

def verify_password(plain_password, hashed_password):
    """验证密码"""
    return pwd_context.verify(plain_password, hashed_password)

def get_user(username: str):
    """根据用户名获取用户"""
    if username in fake_users_db:
        user_data = fake_users_db[username]
        return {"username": user_data["username"], "hashed_password": user_data["hashed_password"]}
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

@app.post("/login", response_model=Token, summary="用户登录")
async def login(user_credentials: UserLogin):
    """
    用户登录接口
    - **username**: 用户名
    - **password**: 密码
    """
    user = authenticate_user(user_credentials.username, user_credentials.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="用户名或密码错误",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/protected", summary="受保护的路由示例")
async def protected_route(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    需要认证才能访问的示例路由
    - 使用 Bearer token 进行认证
    """
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="认证失败")
        
        user = get_user(username)
        if user is None:
            raise HTTPException(status_code=401, detail="用户不存在")
        
        return {"message": f"你好, {username}! 这是一个受保护的路由"}
    
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="无效的令牌")

@app.get("/", summary="健康检查")
async def read_root():
    """API 健康检查端点"""
    return {"message": "FastAPI 认证服务运行正常"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)