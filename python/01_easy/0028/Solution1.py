class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        方法1: 暴力匹配

        思路:
        每次选择原串的一个字符作为「始发点」, 从匹配串的「首位」开始, 二者逐位向后比较
        - 匹配成功, 返回原串「始发点」下标
        - 匹配失败, 选择下一位作为「始发点」, 重新匹配

        时间复杂度: O(n*m), n为原串的长度, m为匹配串的长度
        空间复杂度: O(1)

        :param haystack: str
        :param needle: str
        :return: int
        """
        n, m = len(haystack), len(needle)
        i = 0
        # 如果当前「始发点」后的字符串长度已经小于匹配串长度, 提前结束匹配
        while i + m <= n:
            flag = True
            for j in range(m):
                if haystack[i + j] != needle[j]:
                    flag = False
                    break

            # 匹配成功, 返回原串「始发点」下标
            if flag:
                return i

            # 匹配失败, 选择下一位作为「始发点」, 重新匹配
            i += 1

        return -1

        # if len(haystack) < len(needle):
        #     return -1
        #
        # i = 0
        # while i < len(haystack):
        #     if needle[0] == haystack[i] and len(haystack) - i >= len(needle):
        #         flag = False
        #         k = i
        #
        #         for j in range(len(needle)):
        #             if needle[j] == haystack[k]:
        #                 flag = True
        #             elif needle[j] != haystack[k]:
        #                 flag = False
        #                 break
        #             k += 1
        #
        #         if flag:
        #             return i
        #
        #     i += 1
        #
        # return -1
