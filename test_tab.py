test_tab.py
import random

# 1. 鸡尾酒排序（双向冒泡排序）- 高级优化版本
def bubble_sort(arr):
    """
    鸡尾酒排序（双向冒泡排序）算法实现
    这是冒泡排序的变种，在某些情况下比传统冒泡排序更高效
    :param arr: 待排序的列表
    :return: 排序后的新列表
    """
    # 创建数组副本以避免修改原始数组
    result = arr.copy()
    n = len(result)
    
    # 如果数组长度小于2，直接返回
    if n < 2:
        return result
    
    # 定义左右边界
    left = 0
    right = n - 1
    
    while left < right:
        # 从左到右遍历，将最大值移到右侧
        swapped = False
        for i in range(left, right):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
                swapped = True
        # 最大值已就位，右边界左移
        right -= 1
        
        # 如果没有发生交换，说明数组已经有序
        if not swapped:
            break
        
        # 从右到左遍历，将最小值移到左侧
        swapped = False
        for i in range(right, left, -1):
            if result[i] < result[i - 1]:
                result[i], result[i - 1] = result[i - 1], result[i]
                swapped = True
        # 最小值已就位，左边界右移
        left += 1
        
        # 如果没有发生交换，说明数组已经有序
        if not swapped:
            break

    return result

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

# 4. 堆排序
def heap_sort(arr):
    """
    堆排序算法实现
    :param arr: 待排序的列表
    :return: 排序后的新列表
    """
    def heapify(arr, n, i):
        """
        维护最大堆性质的函数
        :param arr: 数组
        :param n: 堆的大小
        :param i: 当前节点索引
        """
        largest = i  # 初始化最大值为根节点
        left = 2 * i + 1     # 左子节点
        right = 2 * i + 2    # 右子节点

        # 如果左子节点存在且大于根节点
        if left < n and arr[left] > arr[largest]:
            largest = left

        # 如果右子节点存在且大于当前最大值
        if right < n and arr[right] > arr[largest]:
            largest = right

        # 如果最大值不是根节点，则交换并继续堆化
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    # 创建数组副本以避免修改原始数组
    result = arr.copy()
    n = len(result)

    # 构建最大堆
    for i in range(n // 2 - 1, -1, -1):
        heapify(result, n, i)

    # 逐个提取元素从堆中
    for i in range(n - 1, 0, -1):
        # 将当前最大值移到末尾
        result[i], result[0] = result[0], result[i]
        # 对剩余元素进行堆化
        heapify(result, i, 0)

    return result

# 5. 计数排序
def counting_sort(arr):
    """
    计数排序算法实现（适用于非负整数）
    :param arr: 待排序的列表（仅支持非负整数）
    :return: 排序后的新列表
    """
    if not arr:
        return []

    # 找到数组中的最大值和最小值
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1

    # 创建计数数组
    count = [0] * range_val
    output = [0] * len(arr)

    # 统计每个元素出现的次数
    for num in arr:
        count[num - min_val] += 1

    # 计算累积计数
    for i in range(1, range_val):
        count[i] += count[i - 1]

    # 构建输出数组
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1

    return output

# 6. 希尔排序
def shell_sort(arr):
    """
    希尔排序算法实现（插入排序的改进版）
    :param arr: 待排序的列表
    :return: 排序后的新列表
    """
    # 创建数组副本以避免修改原始数组
    result = arr.copy()
    n = len(result)

    # 初始间隔为数组长度的一半，然后逐步缩小
    gap = n // 2

    while gap > 0:
        # 对每个间隔执行插入排序
        for i in range(gap, n):
            temp = result[i]
            j = i

            # 在间隔为gap的子数组中执行插入排序
            while j >= gap and result[j - gap] > temp:
                result[j] = result[j - gap]
                j -= gap

            result[j] = temp

        gap //= 2

    return result
