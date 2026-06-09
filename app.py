from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# 定义登录请求的数据模型
class LoginRequest(BaseModel):
    username: str
    password: str
    email: Optional[str] = None

# 定义响应数据模型
class LoginResponse(BaseModel):
    success: bool
    message: str
    user_id: Optional[int] = None

@app.post("/login", response_model=LoginResponse)
async def login(login_data: LoginRequest):
    """
    处理登录请求
    """
    # 这里是模拟验证逻辑，实际项目中应连接数据库验证
    if login_data.username == "admin" and login_data.password == "password":
        return LoginResponse(
            success=True,
            message="登录成功",
            user_id=12345
        )
    else:
        raise HTTPException(status_code=401, detail="用户名或密码错误")

def quick_sort(arr: list) -> list:
    """
    快速排序算法实现
    
    Args:
        arr: 待排序的列表
        
    Returns:
        排序后的新列表
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # 选取中间元素作为基准
    left = [x for x in arr if x < pivot]      # 小于基准的元素
    middle = [x for x in arr if x == pivot]   # 等于基准的元素
    right = [x for x in arr if x > pivot]     # 大于基准的元素
    
    return quick_sort(left) + middle + quick_sort(right)
@app.get("/")
def read_root():
    return {"message": "欢迎使用FastAPI登录服务"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)