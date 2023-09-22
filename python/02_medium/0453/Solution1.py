from typing import List


class Solution1:
    def minMoves(self, nums: List[int]) -> int:
        #   Args:
        #       nums (List[int]): 进行操作的数组
        #
        #   Returns:
        #       int: 让数组所有元素相等的最小操作次数
        #
        #   方法: 逆向思维
        #
        #   思路:
        #       不考虑元素的 绝对大小 , 而是考虑元素间的 相对大小 ; 那么, 每次操作将 n-1 个元素 加1  <=> 每次操作将 1 个元素 减1 ;
        #       因此, 每次调整的对象只有 1个 并且是 减1操作 , 则总操作次数等于 除了非最小值以外的所有元素 分别通过 减1操作 变成 最小值 所需要的操作次数
        #
        #   时间复杂度: O(n)
        #   空间复杂度: O(1)

        minVal, sumOp = min(nums), 0
        for i in range(len(nums)):
            sumOp += nums[i] - minVal

        return sumOp
