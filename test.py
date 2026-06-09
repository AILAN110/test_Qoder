def quick_sort(arr):
    """
    Return a sorted copy of arr using the quick sort algorithm.
    """
    if len(arr) <= 1:
        return arr.copy()

    pivot = arr[len(arr) // 2]
    left = [item for item in arr if item < pivot]
    middle = [item for item in arr if item == pivot]
    right = [item for item in arr if item > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def bubble_sort_v2(arr):
    """
    Return a sorted copy of arr using an optimized bubble sort algorithm.
    """
    sorted_arr = arr.copy()
    n = len(sorted_arr)

    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True

        if not swapped:
            break

    return sorted_arr


def merge_sort(arr):
    """
    Return a sorted copy of arr using the merge sort algorithm.
    """
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


def bubble_sort_v3(arr):
    print("nihao ")


if __name__ == "__main__":
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", test_array)
    print("Quick sorted array:", quick_sort(test_array))
    print("Bubble sorted array:", bubble_sort_v2(test_array))
    print("Merge sorted array:", merge_sort(test_array))
    print("hello world")
    print("nihao")
