test_tab.py
import random

# 1. 冒泡排序 - 优化版本
def bubble_sort(arr):
    """
    优化的冒泡排序算法实现
    :param arr: 待排序的列表
    :return: 排序后的列表（原地排序）
    """
    n = len(arr)
    # 外层循环控制排序轮数
    for i in range(n):
        # 标记本轮是否发生交换，用于提前结束
        swapped = False
        # 内层循环进行相邻元素比较，每轮后最大元素会移到末尾
        # 所以内层循环范围可逐渐减小 (n - i - 1)
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # 交换相邻元素
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # 如果本轮没有发生交换，说明数组已经有序，可以提前结束
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

# 3. 归并排序
def merge_sort(arr):
    """
    归并排序算法实现
    :param arr: 待排序的列表
    :return: 排序后的新列表
    """
    if len(arr) <= 1:
        return arr
    
    # 分割数组为两半
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # 递归排序两半
    left = merge_sort(left)
    right = merge_sort(right)
    
    # 合并已排序的两半
    return merge(left, right)

def merge(left, right):
    """
    合并两个已排序的列表
    :param left: 左侧已排序的列表
    :param right: 右侧已排序的列表
    :return: 合并后的已排序列表
    """
    result = []
    i = j = 0
    
    # 比较两个列表中的元素并按顺序合并
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # 添加剩余的元素
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result