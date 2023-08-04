from Solution1 import Solution1


def main():
    # 输入
    strs = [["flower", "flow", "flight"],
            ["dog", "rececar", "car"],
            ["ab", "a"]]
    # 期望输出
    output = ["fl", "", "a"]
    # 选择方法
    solution = Solution1()

    for i, sList in enumerate(strs):
        print("输入: strs = [", end='')
        for j, s in enumerate(sList):
            print("\"{}\"".format(s), end='')
            if j != len(sList) - 1:
                print(", ", end='')
            else:
                print("]")
        print("输出: \"{}\"".format(solution.longestCommonPrefix(sList)))
        print("期望输出：\"{}\"".format(output[i]))
        print()


if __name__ == '__main__':
    main()
