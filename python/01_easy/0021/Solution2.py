from typing import Optional


# 单链表定义
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        方法1: 递归

        思路: 将问题逐步细分为子问题, 比如: 当合并l1与l2时, 假设此时l1更小, 那么l1一定先放入新链表; 此时, 合并l1与l2等价于
        先合并l1->next与l2, 然后让l1指向l1->next与l2的合并结果

        如果定义"()"为合并操作, 当l1.val<l2.val时, (l1, l2) <==> l1.next = (l1.next, l2)

        终止条件是链表为空, 代表此链表已完成合并了

        时间复杂度: O(m+n)
        空间复杂度: O(m+n), 递归需要栈, 叠加深度最差情况为两个链表长度之和

        :param list1: Optional[ListNode]
        :param list2: Optional[ListNode]
        :return: Optional[ListNode]
        """

        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list2.next, list1)
            return list2
