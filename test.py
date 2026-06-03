def bubble_sort(arr):
    """
    冒泡排序算法
    
    参数:
        arr: 待排序的列表
    
    返回:
        排序后的列表
    """
    n = len(arr)
    
    # 遍历所有数组元素
    for i in range(n):
        # 标记是否发生了交换
        swapped = False
        
        # 最后i个元素已经排好序了
        for j in range(0, n - i - 1):
            # 如果当前元素大于下一个元素，则交换
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # 如果没有发生交换，说明数组已经有序
        if not swapped:
            break
    
    return arr


# 测试示例
if __name__ == "__main__":
    test_list = [64, 34, 25, 12, 22, 11, 90]
    print("原始列表:", test_list)
    
    sorted_list = bubble_sort(test_list.copy())  # 使用copy()避免修改原列表
    print("排序后列表:", sorted_list)