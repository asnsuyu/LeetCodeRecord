from Solution1 import Solution1


def main():
    # 输入数组
    numss = [[], [1, 2, 3], [1, 1, 2], [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]]
    # 长度正确的期望答案
    expectedNumss = [[], [1, 2, 3], [1, 2], [0, 1, 2, 3, 4]]

    # 调用
    solution = Solution1()
    for i, nums in enumerate(numss):
        k = solution.removeDuplicates(nums)

        assert k == len(expectedNumss[i])
        for j in range(k):
            assert nums[j] == expectedNumss[i][j]


if __name__ == '__main__':
    main()
