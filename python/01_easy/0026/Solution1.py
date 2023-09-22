from typing import List


class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        方法1: 双指针

        思路: 使用两个指针, 旨在不断将右侧第一次出现的元素覆盖掉左侧的重复元素. 慢指针记录目标排序的最后位置, 快指针用于观测

        时间复杂度: O(n)
        空间复杂度: O(1)

        :param nums: List[int]
        :return: int
        """

        # 数组长度为0, 返回0
        if len(nums) == 0:
            return 0

        # i指向从左往右已去除重复元素排列中的最后一个元素位置
        # j用于观测与nums[i]不同的元素, 若找到, 放在i+1位置
        i, j = 0, 1
        while j < len(nums):
            if nums[i] != nums[j]:
                nums[i + 1] = nums[j]
                i += 1
            j += 1

        # i指向目标排序中的最后元素, 返回长度为i+1
        return i + 1
