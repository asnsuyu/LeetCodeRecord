class Solution1:
    def isValid(self, s: str) -> bool:
        """
        方法一: 使用栈进行匹配

        思路: 利用栈存储需要匹配的括号; 若为左括号, 入栈; 若为右括号, 弹出栈顶与之比较

        时间复杂度: O(n)
        空间复杂度: O(n)

        :param s: str
        :return: bool
        """

        # 括号匹配规则
        match = {
            '(': ')',
            '[': ']',
            '{': '}',
            # 增加'?'规则是为了先将其放入栈中, 防止后续出现pop空栈错误
            '?': '?'
        }

        stack = ['?']
        for i in range(len(s)):
            # 若s[i]为左括号, 则入栈
            if s[i] in match:
                stack.append(s[i])
            # 否则, 先出栈, 然后用出栈值与s[i]进行匹配
            else:
                if match[stack.pop()] != s[i]:
                    return False

        # 因为预先放入了'?', 最后检查栈长度是否为1; 不为1, 说明左括号多了
        return len(stack) == 1
