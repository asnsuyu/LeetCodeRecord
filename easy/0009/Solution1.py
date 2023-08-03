class Solution1:
    def isPalindrome(self, x: int) -> bool:
        """
        方法一：转化成字符串

        思路：将输入x转化为字符串，然后头尾进行比较

        时间复杂度：O(n^2)
        空间复杂度：O(1)

        :param x: int
        :return: bool
        """

        s = str(x)
        return s == s[::-1]
