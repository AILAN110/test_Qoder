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


if __name__ == "__main__":
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", test_array)
    print("Sorted array:", quick_sort(test_array))
