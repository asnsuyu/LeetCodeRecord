from Solution1 import Solution1
from Solution2 import Solution2


def main():
    # 输入数组
    numss = [[3, 2, 2, 3], [0, 1, 2, 2, 3, 0, 4, 2]]
    vals = [3, 2]
    # 长度正确的期望答案
    expectedNumss = [[2, 2], [0, 1, 3, 0, 4]]

    # 调用
    solution = Solution1()
    # solution = Solution2()
    for i, nums in enumerate(numss):
        k = solution.removeElement(nums, vals[i])

        assert k == len(expectedNumss[i])  # 检测长度是否一致
        for j in range(k):
            assert nums[j] == expectedNumss[i][j]  # 检测元素是否一致


if __name__ == '__main__':
    main()
