def quick_sort(arr):
    """
    快速排序算法
    
    Args:
        arr: 待排序的列表
    
    Returns:
        排序后的新列表
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # 选择中间元素作为基准
    left = [x for x in arr if x < pivot]    # 小于基准的元素
    middle = [x for x in arr if x == pivot] # 等于基准的元素
    right = [x for x in arr if x > pivot]   # 大于基准的元素
    
    # 递归排序左右两部分，并合并结果
    return quick_sort(left) + middle + quick_sort(right)

def bubble_sort(arr):
    """
    冒泡排序算法（示例对比）
    
    Args:
        arr: 待排序的列表
    
    Returns:
        排序后的列表（原地修改）
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 测试代码
if __name__ == "__main__":
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", test_array)
    
    sorted_array = quick_sort(test_array.copy())
    print("快速排序结果:", sorted_array)
    
    bubble_sorted = bubble_sort(test_array.copy())
    print("冒泡排序结果:", bubble_sorted)

    '''
    {
        "human_additions":48,
        "unknown_additions":0,
        "ai_additions":0,
        "ai_accepted":0,
        "git_diff_deleted_lines":0,
        "git_diff_added_lines":48,
        "tool_model_breakdown":{}
    }
    '''