from Solution1 import Solution1


def main():
    # 输入
    nums = [1, 3, 5, 6]
    targets = [5, 2, 7]
    # 期望输出
    expectedOutputs = [2, 1, 4]
    # 调用
    solution = Solution1()
    for i, target in enumerate(targets):
        assert solution.searchInsert(nums, target) == expectedOutputs[i]
        # assert solution.binarySearch(nums, target, 0, len(nums) - 1) == expectedOutputs[i]


if __name__ == '__main__':
    main()
