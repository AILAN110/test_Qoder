import random

# 1. 冒泡排序
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# 2. 快速排序
def quick_sort(arr):
    """
    快速排序算法实现
    :param arr: 待排序的列表
    :return: 排序后的新列表
    """
    if len(arr) <= 1:
        return arr
    
    # 选择基准元素（这里选择中间位置的元素）
    pivot = arr[len(arr) // 2]
    
    # 分割数组为三部分：小于基准、等于基准、大于基准
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # 递归排序左右两部分，并合并结果
    return quick_sort(left) + middle + quick_sort(right)