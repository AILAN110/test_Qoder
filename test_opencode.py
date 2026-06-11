import random


def generate_random_array(length=10, min_val=0, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(length)]


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print("")