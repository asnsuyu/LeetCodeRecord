from typing import List


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        方法二：查找表法

        思路：类似方法一的思路，也需要寻找差值；但是方法二用一个额外空间存储已经遍历的数字，这样寻找差值时，
        只需要在已经遍历的数字寻找即可；方法一每次查询差值需要遍历后续数组，而方法二利用哈希表查询差值只需要O(1)的时间复杂度

        时间复杂度：O(n)
        空间复杂度：O(n)

        :param nums: List[int]
        :param target: int
        :return: List[int]
        """

        # 创建一个用来存储数组中已经遍历过的数字的字典（模拟哈希表）
        hashtable = {}
        # 遍历数组
        for i, num in enumerate(nums):
            # 计算需要寻找的另一个数字的值：find
            find = target - num
            # 若在后续数组中存在，则返回
            if find in hashtable:
                # 哈希表中存储的是已经遍历过的数字，这些数字在原数组中位置更靠前，是需要先返回的下标
                return [hashtable[find], i]
            # 未找到find，将此次遍历数字存入哈希表；i=0时，哈希表为空，会直接放入
            hashtable[num] = i

        # 数组中未找到和为target的两个数字，返回空列表
        return []
