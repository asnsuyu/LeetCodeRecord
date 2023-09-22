from Solution1 import Solution1


def main():
    # 输入
    numss = [[4, 2, 3], [4, 2, 1], [3, 4, 2, 3], [5, 7, 1, 8]]
    # 期望输出
    expectedOutputs = [True, False, False, True]
    # 调用
    solution = Solution1()
    for i, nums in enumerate(numss):
        assert solution.checkPossibility(nums) == expectedOutputs[i]


if __name__ == '__main__':
    main()
