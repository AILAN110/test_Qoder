"""
递归算法演示程序
包含阶乘函数的递归实现和二分排序函数
"""

def factorial(n: int) -> int:
    """
    计算阶乘的递归实现
    
    Args:
        n: 非负整数
        
    Returns:
        n的阶乘值
    """
    if n < 0:
        raise ValueError("输入必须为非负整数")
    
    # 基础情况：0! = 1, 1! = 1
    if n == 0 or n == 1:
        return 1
    
    # 递归情况：n! = n * (n-1)!
    return n * factorial(n - 1)


def binary_insertion_sort(arr: list) -> list:
    """
    二分插入排序算法
    
    该算法使用二分查找来确定插入位置，相比普通插入排序减少了比较次数
    
    Args:
        arr: 需要排序的列表
        
    Returns:
        排序后的列表
    """
    for i in range(1, len(arr)):
        key = arr[i]
        # 使用二分查找找到插入位置
        left, right = 0, i - 1
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > key:
                right = mid - 1
            else:
                left = mid + 1
        
        # 将元素插入到正确位置
        arr[i + 1:left:-1] = arr[i:left:-1]
        arr[left] = key
    
    return arr


def main():
    """主函数，演示阶乘递归算法和二分排序"""
    print("=== 阶乘递归算法演示 ===\n")
    
    # 演示阶乘计算
    print("阶乘计算:")
    for i in range(6):
        print(f"{i}! = {factorial(i)}")
    
    print("\n=== 二分排序算法演示 ===\n")
    
    # 演示二分排序
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"原始数组: {test_arr}")
    sorted_arr = binary_insertion_sort(test_arr.copy())
    print(f"排序后数组: {sorted_arr}")


if __name__ == "__main__":
    main()