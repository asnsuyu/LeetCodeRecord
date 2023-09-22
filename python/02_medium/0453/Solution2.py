from typing import List


class Solution2:
    def minMoves(self, nums: List[int]) -> int:
        #   Args:
        #       nums (List[int]): 进行操作的数组
        #
        #   Returns:
        #       int: 让数组所有元素相等的最小操作次数
        #
        #   方法: 数学公式推导
        #
        #   思路:
        #       设, 原数组总和为sum, 原数组最小值为min, 元素个数为n, 最小操作次数为m, 最终数组中所有元素的值都被调整为x, 那么有下列等式:
        #       sum+m*(n-1)=n*x : (1), 即每次让 n-1 个数加1, 调整 m 次就是让整体数组总和增加了 m*(n-1) , 最终, 原数组总和+增加的值=目标数组总和
        #
        #       又因为, 原数组中的最小值 min 最后一定会被调整为目标数组中的目标值 x , 因此一定满足下面的关系:
        #       min+m=x : (2), 即最小值 min 通过 m 次加1操作最终会变为 x
        #
        #       将公式(2)代入公式(1)可得:
        #       m=sum-n*min, 即最终要求的最小操作数可以通过 原数组总和、数组长度、最小值 三个值直接计算得到
        #
        #   时间复杂度: O(n)
        #   空间复杂度: O(1)

        sumVal, n, minVal = sum(nums), len(nums), min(nums)
        return sumVal - n * minVal
