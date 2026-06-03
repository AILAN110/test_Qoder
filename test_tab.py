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
    改进的归并排序算法实现
    :param arr: 待排序的列表
    :return: 排序后的新列表
    """
    if len(arr) <= 1:
        return arr

    def merge_sort_helper(arr, temp_arr, left, right):
        """
        归并排序的递归辅助函数
        :param arr: 原始数组
        :param temp_arr: 临时数组，用于合并过程
        :param left: 左边界
        :param right: 右边界
        """
        if left >= right:
            return

        mid = (left + right) // 2
        # 递归排序左半部分
        merge_sort_helper(arr, temp_arr, left, mid)
        # 递归排序右半部分
        merge_sort_helper(arr, temp_arr, mid + 1, right)
        # 合并已排序的两部分
        merge(arr, temp_arr, left, mid, right)

    def merge(arr, temp_arr, left, mid, right):
        """
        合并两个已排序的子数组
        :param arr: 原始数组
        :param temp_arr: 临时数组
        :param left: 左边界
        :param mid: 中点
        :param right: 右边界
        """
        # 复制数据到临时数组
        for i in range(left, right + 1):
            temp_arr[i] = arr[i]

        i = left      # 左子数组的开始
        j = mid + 1   # 右子数组的开始
        k = left      # 合并后数组的开始

        # 合并两个子数组
        while i <= mid and j <= right:
            if temp_arr[i] <= temp_arr[j]:
                arr[k] = temp_arr[i]
                i += 1
            else:
                arr[k] = temp_arr[j]
                j += 1
            k += 1

        # 复制左子数组的剩余元素
        while i <= mid:
            arr[k] = temp_arr[i]
            i += 1
            k += 1

        # 复制右子数组的剩余元素
        while j <= right:
            arr[k] = temp_arr[j]
            j += 1
            k += 1

    # 创建数组副本以避免修改原始数组
    result = arr.copy()
    # 创建临时数组用于合并过程
    temp_arr = [0] * len(result)
    # 执行归并排序
    merge_sort_helper(result, temp_arr, 0, len(result) - 1)
    return result