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

def quick_sort(arr):
    """
    使用递归方法实现快速排序算法
    
    Args:
        arr: 待排序的列表
    
    Returns:
        排序后的新列表
    """
    # 递归基础情况：如果数组长度小于等于1，直接返回
    if len(arr) <= 1:
        return arr
    
    # 选择基准值（这里选择中间元素）
    pivot = arr[len(arr) // 2]
    
    # 分割数组
    left = [x for x in arr if x < pivot]      # 小于基准值的元素
    middle = [x for x in arr if x == pivot]   # 等于基准值的元素
    right = [x for x in arr if x > pivot]     # 大于基准值的元素
    
    # 递归排序并合并结果
    return quick_sort(left) + middle + quick_sort(right)


# 示例用法
if __name__ == "__main__":
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("原数组:", test_array)
    sorted_array = quick_sort(test_array)
    print("排序后:", sorted_array)
    # 计算1到200的累加和
    sum_1_to_200 = recursive_sum(200)
