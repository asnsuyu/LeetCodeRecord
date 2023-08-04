from Solution1 import Solution1


def main():
    # 输入
    s = ["()", "()[]{}", "(]"]
    # 期望输出
    output = ["true", "true", "false"]
    # 选择方法
    solution = Solution1()

    for i, ss in enumerate(s):
        print("输入: s = \"{}\"".format(ss))
        print("输出: {}".format("true" if solution.isValid(ss) else "false"))
        print("期望输出: {}".format(output[i]), end='{}'.format('\n\n' if i != len(s) - 1 else '\n'))


if __name__ == '__main__':
    main()
