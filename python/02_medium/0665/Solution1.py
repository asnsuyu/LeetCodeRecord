from typing import List


class Solution1:
    def checkPossibility(self, nums: List[int]) -> bool:
        #   Args:
        #       nums (List[int]): 需要进行判断的数组
        #
        #   Returns:
        #       bool: 返回判断结果, 是否可以通过指定操作将输入数组变为非递减数列
        #
        #   方法: 瞻前顾后, 贪心
        #
        #   思路:
        #       每次遍历时需要同时考虑三个元素: nums[i-1], nums[i], nums[i+1]
        #       当出现 nums[i]>nums[i+1] 即递减情况时, 第一反应是缩小 nums[i] 以满足 nums[i]<=nums[i+1] , 会直接选择把 nums[i] 缩小为 nums[i+1]
        #       这一步的易错点在于: 当我们将 nums[i] 缩小为 nums[i+1] 时, 如果 nums[i-1] > nums[i+1], 会导致新的递减情况即 nums[i-1] > nums[i]
        #
        #       因此, 当出现递减情况 nums[i]>nums[i+1] 时, 需要同时考虑 nums[i-1] ,
        #       从而根据实际情况选择是 将nums[i]缩小为nums[i+1] 还是 将nums[i+1]增大为nums[i]
        #
        #       同时要记录修改次数防止多次修改
        #
        #   时间复杂度: O(n)
        #   空间复杂度: O(n)

        # 利用切片复制nums得到副本, 实现值传递, 防止修改原数组
        # count用来记录修改次数, 检测是否还能修改
        numsCopy, i, count = nums[:], 0, 0
        while i < len(numsCopy) - 1:
            if numsCopy[i] > numsCopy[i + 1]:
                # count值代表这是第几次修改
                count += 1
                # count=2, 这是第2次修改, 不满足题意直接返回
                if count > 1:
                    return False

                # 出现递减情况同时要考虑nums[i-1]这个元素
                if i != 0 and numsCopy[i - 1] > numsCopy[i + 1]:
                    # nums[i-1]>nums[i+1], 选择将 nums[i+1]放大为nums[i]
                    numsCopy[i + 1] = numsCopy[i]
                else:
                    # nums[i-1]<=nums[i+1], 选择将 nums[i]缩小为nums[i+1]
                    numsCopy[i] = numsCopy[i + 1]

            i += 1

        return True
