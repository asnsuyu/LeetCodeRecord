from Solution1 import Solution1
from Solution2 import Solution2


def main():
    # 输入
    nums = [[2, 7, 11, 15],
            [3, 2, 4],
            [3, 3]]
    target = [9, 6, 6]
    # 期望输出
    output = [[0, 1],
              [1, 2],
              [0, 1]]
    # 选择方法
    # solution = Solution1()
    solution = Solution2()

    for i, row in enumerate(nums):
        print("输入: nums = {}, target = {}".format(row, target[i]))
        print("输出: {}".format(solution.twoSum(row, target[i])))
        print("期望输出: {}".format(output[i]))
        print()


if __name__ == '__main__':
    main()
