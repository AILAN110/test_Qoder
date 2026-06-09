"""
递归算法演示程序
仅包含阶乘函数的递归实现
"""

def factorial(n: int) -> int:
    """
    计算阶乘的递归实现
    
    Args:
        n: 非负整数
        
    Returns:
        n的阶乘值
    """
    if n < 0:
        raise ValueError("输入必须为非负整数")
    
    # 基础情况：0! = 1, 1! = 1
    if n == 0 or n == 1:
        return 1
    
    # 递归情况：n! = n * (n-1)!
    return n * factorial(n - 1)


def main():
    """主函数，演示阶乘递归算法"""
    print("=== 阶乘递归算法演示 ===\n")
    
    # 演示阶乘计算
    print("阶乘计算:")
    for i in range(6):
        print(f"{i}! = {factorial(i)}")


if __name__ == "__main__":
    main()