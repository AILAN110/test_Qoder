def quick_sort(arr):
    """
    快速排序算法实现
    
    参数:
    arr (list): 需要排序的列表
    
    返回:
    list: 排序后的列表
    """
    if len(arr) <= 1:
        return arr
    
    # 选择基准元素
    pivot = arr[len(arr) // 2]
    
    # 分区操作
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # 递归排序
    return quick_sort(left) + middle + quick_sort(right)

# 示例用法
if __name__ == "__main__":
    test_array = [3, 6, 8, 10, 1, 2, 1]
    print("原始数组:", test_array)
    sorted_array = quick_sort(test_array)
    print("排序后数组:", sorted_array)
    print("hello, world!")
    '''
    {
        "human_additions":31,
        "unknown_additions":0,
        "ai_additions":0,
        "ai_accepted":0,
        "git_diff_deleted_lines":0,
        "git_diff_added_lines":31,
        "tool_model_breakdown":{}
    }
    '''