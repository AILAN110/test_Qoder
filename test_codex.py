import random


print("")


def generate_random_sequence(length, start=0, end=100):
    """Return a list of random integers within the inclusive range."""
    return [random.randint(start, end) for _ in range(length)]


def bubble_sort(items):
    """Return a new list sorted in ascending order using bubble sort."""
    result = list(items)
    length = len(result)

    for i in range(length):
        swapped = False
        for j in range(0, length - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True

        if not swapped:
            break

    return result
