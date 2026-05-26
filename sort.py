def merge_sort(arr):
    """
    归并排序算法实现
    
    Args:
        arr: 待排序的列表
    
    Returns:
        排序后的新列表（不修改原列表）
    """
    if len(arr) <= 1:
        return arr

    # 分割数组
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # 合并两个已排序的子数组
    return _merge(left_half, right_half)


def _merge(left, right):
    """
    合并两个已排序的列表
    
    Args:
        left: 左侧已排序列表
        right: 右侧已排序列表
    
    Returns:
        合并后的已排序列表
    """
    merged = []
    i = j = 0

    # 比较并合并
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # 添加剩余元素
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged


# 测试归并排序
if __name__ == "__main__":
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", test_array)
    
    sorted_array = merge_sort(test_array)
    print("排序后数组:", sorted_array)