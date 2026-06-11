def sort_list(items, reverse=False):
    """对列表进行排序，返回新列表（不修改原列表）。"""
    return sorted(items, reverse=reverse)


def sort_dict_list(items, key, reverse=False):
    """按字典的某个键对字典列表排序。"""
    return sorted(items, key=lambda x: x[key], reverse=reverse)


if __name__ == "__main__":
    nums = [3, 1, 4, 1, 5, 9, 2, 6]
    print(sort_list(nums))
    print(sort_list(nums, reverse=True))

    users = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
    ]
    print(sort_dict_list(users, key="age"))
