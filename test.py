def bubble_sort(arr):
    """
    冒泡排序算法实现
    
    参数:
        arr: 待排序的列表
    
    返回:
        排序后的列表
    """
    n = len(arr)
    
    # 遍历所有数组元素
    for i in range(n):
        # 标记是否发生了交换，用于优化
        swapped = False
        
        # 最后i个元素已经排好序了
        for j in range(0, n - i - 1):
            # 如果当前元素比下一个元素大，则交换
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # 如果没有发生交换，说明数组已经有序，可以提前退出
        if not swapped:
            break
    
    return arr

# 测试代码
if __name__ == "__main__":
    # 测试用例
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", test_array)
    
    sorted_array = bubble_sort(test_array.copy())  # 使用copy()避免修改原数组
    print("排序后数组:", sorted_array)
    
    # 其他测试用例
    print("\n其他测试用例:")
    print("空数组:", bubble_sort([]))
    print("单个元素:", bubble_sort([1]))
    print("已排序数组:", bubble_sort([1, 2, 3, 4, 5]))
    print("逆序数组:", bubble_sort([5, 4, 3, 2, 1]))
    print("重复元素:", bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]))