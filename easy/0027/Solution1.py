from typing import List


class Solution1:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        方法1: 双指针

        思路:
        先设定变量 idx, 指向待插入位置. idx 初始值为0
        - 两个指针都是从左向右开始遍历
        - 如果当前元素 x 与移除元素 val 相同, 那么跳过该元素
        - 如果当前元素 x 与移除元素 val 不同, 那么将其放到下标 idx 的位置, 并让 idx 自增右移
        最终得到的 idx 即为答案

        时间复杂度: O(n)
        空间复杂度: O(1)

        :param nums: List[int]
        :param val: int
        :return: int
        """
        idx = 0
        for x in nums:
            if x != val:
                nums[idx] = x
                idx += 1

        return idx
