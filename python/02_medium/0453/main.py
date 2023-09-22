from Solution1 import Solution1
from Solution2 import Solution2


def main():
    # 输入
    numss = [[1, 2, 3], [1, 1, 1]]
    # 期望输出
    expectedOutputs = [3, 0]
    # 调用
    # solution = Solution1()
    solution = Solution2()
    for i, nums in enumerate(numss):
        assert solution.minMoves(nums) == expectedOutputs[i]


if __name__ == '__main__':
    main()
