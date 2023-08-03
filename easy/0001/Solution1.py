class Solution1:
    def twoSum(self, nums, target):
        """
        方法一：暴力求解

        思路：遍历数组，同时寻找target与当前指向数字的差值（要找的第二个数字）是否在后续数组中；
        存在，则返回二者下标；不存在，继续遍历，全部遍历后仍不存在，则返回空列表

        时间复杂度：O(n^2)
        空间复杂度：O(1)

        :param nums: List[int]
        :param target: int
        :return: List[int]
        """

        # 遍历数组
        for i in range(len(nums)):
            # 计算需要寻找的另一个数字的值：find
            find = target - nums[i]
            # 若在后续数组中存在，则返回
            if find in nums[i + 1:]:
                # 使用index()方法返回find在nums[i+1:]中的下标，加上i+1得到在原数组中的下标
                return [i, nums[i + 1:].index(find) + i + 1]

        # 数组中未找到和为target的两个数字，返回空列表
        return []
