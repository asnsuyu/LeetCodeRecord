from Solution1 import Solution1


def main():
    # 输入
    s = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
    # 期望输出
    output = [3, 4, 9, 58, 1994]
    # 选择方法
    solution = Solution1()

    for i, rStr in enumerate(s):
        print("输入: s = \"{}\"".format(rStr))
        print("输出: {}".format(solution.romanToInt(rStr)))
        print("期望输出: {}".format(output[i]))
        print()


if __name__ == '__main__':
    main()
