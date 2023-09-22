from typing import List


class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        方法1: 双指针

        思路:
        将数组分为「前后」两段:
        - 前半段是有效部分, 存储的是 不等于 val 的元素
        - 后半段是无效部分, 存储的是 等于 val 的元素
        通过 swap 操作将后半段中的有效元素交换到前半段中来, 题目并未要求输出数组是固定顺序, 因此可行
        最终答案返回有效部分的结尾下标

        时间复杂度: O(n)
        空间复杂度: O(1)

        :param nums: List[int]
        :param val: int
        :return: int
        """
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[i] == val:
                self.swap(nums, i, j)
                i -= 1  # 每次交换后 i--, 防止交换过来的 nums[j] 仍然是 val 而错过判断
                j -= 1
            i += 1

        return j + 1

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
