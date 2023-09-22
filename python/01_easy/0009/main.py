from Solution1 import Solution1


def main():
    # 输入
    x = [121, -121, 10]
    # 期望输出
    output = [True, False, False]
    # 选择方法
    solution = Solution1()

    for i, num in enumerate(x):
        print("输入: x = {}".format(num))
        print("输出: {}".format(solution.isPalindrome(num)))
        print("期望输出: {}".format(output[i]))
        print()


if __name__ == '__main__':
    main()
