def bubble_sort(arr):
    """
    冒泡排序算法实现
    
    Args:
        arr: 待排序的列表
    
    Returns:
        排序后的新列表（不修改原列表）
    """
    # 创建原数组的副本，避免修改原列表
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    
    # 外层循环控制排序轮数
    for i in range(n):
        # 标记本轮是否发生交换（优化用）
        swapped = False
        
        # 内层循环进行相邻元素比较
        # 每轮结束后最大元素会"冒泡"到末尾，所以范围逐渐缩小
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                # 交换相邻元素
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        
        # 如果本轮没有发生交换，说明已经有序，提前结束
        if not swapped:
            break
    
    return sorted_arr


# 测试冒泡排序
if __name__ == "__main__":
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", test_array)
    
    sorted_array = bubble_sort(test_array)
    print("排序后数组:", sorted_array)