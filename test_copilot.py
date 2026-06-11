def sort_numbers(numbers):
    """Sort a list of numbers in ascending order."""
    return sorted(numbers)


def sort_strings(strings):
    """Sort a list of strings alphabetically."""
    return sorted(strings)


def sort_descending(numbers):
    """Sort a list of numbers in descending order."""
    return sorted(numbers, reverse=True)


if __name__ == "__main__":
    # Test examples
    nums = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"Original: {nums}")
    print(f"Sorted ascending: {sort_numbers(nums)}")
    print(f"Sorted descending: {sort_descending(nums)}")

    words = ["banana", "apple", "cherry", "date"]
    print(f"Words sorted: {sort_strings(words)}")
