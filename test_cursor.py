def bubble_sort(arr):
    """冒泡排序：相邻元素比较并交换，较大元素逐步"冒泡"到末尾。"""
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

def test():
    print("hello")

if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("排序前:", data)
    bubble_sort(data)
    print("排序后:", data)
    test()
