class Solution1:
    def romanToInt(self, s: str) -> int:
        """
        方法一：

        思路：建立罗马字符与自然数的映射关系，遍历字符串，分别将每个字符转化为对应的自然数并进行累加；
        累加时要注意特殊规则：当第i个数字大于第i+1个数字时，正常累加；若小于，则加上第i个数字的负值

        时间复杂度：O(n)
        空间复杂度：O(1)

        :param s: str
        :return: int
        """

        # 定义罗马字符与自然数字对应关系
        match = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        i = 0
        result = 0  # 存放最终结果
        # 因为每次累加会用当前数字与后一个数字比较，为防止越界设置i<len(s)-1
        while i < len(s) - 1:
            # 当前数字
            num = match[s[i]]
            # 比较当前数字与后一个数字大小
            if num < match[s[i + 1]]:
                # 比后一个小，则当前数字取负值
                result -= num
            else:
                # 比后一个大，则当前数字取正值
                result += num
            i += 1
        # 为防止越界，数组最后一个数字无法与后一个数字比较，需单独累加
        result += match[s[i]]

        return result
