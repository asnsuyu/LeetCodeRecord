from typing import List


class Solution1:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        方法1: 二分查找法

        思路: 使用二分查找法, 每次丢弃一半的查找空间, 加快查找速度


        时间复杂度: O(logn)
        空间复杂度: O(1)

        :param nums: List[int]
        :param target: int
        :return: int
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            # 设置中间分割点
            middel = (left + right) // 2

            if target < nums[middel]:
                # 目标在分割点左侧, 丢弃右半查找空间
                right = middel - 1
            elif target > nums[middel]:
                # 目标在分割点右侧, 丢弃左半查找空间
                left = middel + 1
            else:
                # 目标等于分割点, 返回分割点下标
                return middel

        # left > right, 则返回left
        return left

        # k = self.binarySearch(nums, target, 0, len(nums) - 1)
        #
        # return k

    # def binarySearch(self, nums, target, left, right):
    #     if left <= right:
    #         middle = (left + right) // 2
    #
    #         if target < nums[middle]:
    #             return self.binarySearch(nums, target, left, middle - 1)
    #         elif target > nums[middle]:
    #             return self.binarySearch(nums, target, middle + 1, right)
    #         else:
    #             return middle
    #
    #     return left
