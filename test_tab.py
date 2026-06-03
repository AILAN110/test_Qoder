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
    改进的快速排序算法实现（原地排序，随机化基准）
    :param arr: 待排序的列表
    :return: 排序后的新列表
    """
    import random
    
    # 创建数组副本以避免修改原始数组
    result = arr.copy()
    
    def randomized_partition(low, high):
        """
        随机化分区函数
        :param low: 分区起始索引
        :param high: 分区结束索引
        :return: 分区点索引
        """
        # 随机选择基准元素并与最后一个元素交换
        random_index = random.randint(low, high)
        result[random_index], result[high] = result[high], result[random_index]
        
        pivot = result[high]
        i = low - 1  # 较小元素的索引
        
        for j in range(low, high):
            if result[j] <= pivot:
                i += 1
                result[i], result[j] = result[j], result[i]
        
        result[i + 1], result[high] = result[high], result[i + 1]
        return i + 1

    def quick_sort_recursive(low, high):
        """
        快速排序的递归实现
        :param low: 排序范围的起始索引
        :param high: 排序范围的结束索引
        """
        if low < high:
            # 获取分区索引
            pi = randomized_partition(low, high)
            
            # 递归排序基准前后的子数组
            quick_sort_recursive(low, pi - 1)
            quick_sort_recursive(pi + 1, high)

    if len(result) > 1:
        quick_sort_recursive(0, len(result) - 1)
    
    return result

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