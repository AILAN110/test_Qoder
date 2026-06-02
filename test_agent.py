def solve_chicken_rabbit(heads, legs):
    """
    解鸡兔同笼问题
    假设：每只鸡 1 个头 2 条腿，每只兔 1 个头 4 条腿
    参数:
        heads: 总头数
        legs: 总腿数
    返回:
        (chickens, rabbits): 鸡和兔的数量元组
        若无整数解则返回 (None, None)
    """
    # 公式推导：
    # 设鸡 x 只，兔 y 只
    # x + y = heads
    # 2x + 4y = legs
    # 解得：y = (legs - 2*heads) / 2, x = heads - y
    rabbits = (legs - 2 * heads) / 2
    chickens = heads - rabbits

    # 检查是否为非负整数
    if rabbits < 0 or chickens < 0 or not rabbits.is_integer() or not chickens.is_integer():
        return None, None

    return int(chickens), int(rabbits)


def main():
    print("=" * 30)
    print("     鸡兔同笼问题求解")
    print("=" * 30)

    try:
        heads = int(input("请输入总头数: "))
        legs = int(input("请输入总腿数: "))

        if heads <= 0 or legs <= 0:
            print("头数和腿数必须为正整数！")
            return

        chickens, rabbits = solve_chicken_rabbit(heads, legs)

        if chickens is None:
            print("无解！请检查输入的头数和腿数是否合理。")
        else:
            print(f"\n求解结果：")
            print(f"鸡的数量：{chickens} 只")
            print(f"兔的数量：{rabbits} 只")
            # 验证
            print(f"\n验证：总头数 {chickens + rabbits}，总腿数 {chickens*2 + rabbits*4}")

    except ValueError:
        print("输入错误，请输入整数！")


if __name__ == "__main__":
    main()