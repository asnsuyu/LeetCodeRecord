from typing import List


class Solution1:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        方法一: 纵向比较法

        思路: 想象将数组中所有字符串左对齐排成一列, 依次对比所有字符串第1, 2, ...列对应的所有字符是否相同

        时间复杂度: O(mn), m为字符串数组中字符串的平均长度, n为数组长度
        空间复杂度: O(1)

        :param strs: List[str]
        :return: str
        """

        # 输入的不是字符串数组, 返回空串
        if not strs:
            return ""

        # 记录第1个字符串长度, 字符串数组个数
        length, count = len(strs[0]), len(strs)
        # i用来指向当前各字符串比较到第几个字符了
        for i in range(length):
            # 记录各字符串正在比较的字符
            ch = strs[0][i]
            # j用来指向正在与第1个字符串进行比较的字符串
            for j in range(1, count):
                # 与第1个字符串进行比较的字符串长度更短 || 当前比较的字符已经不同了, 返回0~i-1范围的字符串
                # 条件1必须放在or前, 防止数组下标越界
                if i == len(strs[j]) or ch != strs[j][i]:
                    return strs[0][:i]

        # 中途比较全部进行完毕, 说明strs[0]自身即为最长公共前缀, 返回自身
        return strs[0]
