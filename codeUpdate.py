def recursive_sum(n):
    """
    使用递归方法计算从1到n的累加和
    
    Args:
        n: 计算到第n个数字
    
    Returns:
        从1到n的累加和
    """
    # 递归基础情况：当n为1时，返回1
    if n <= 1:
        return n
    # 递归情况：n + (1到n-1的累加和)
    else:
        return n + recursive_sum(n - 1)

# 计算1到200的累加和
sum_1_to_200 = recursive_sum(200)
