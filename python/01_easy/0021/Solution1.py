from typing import Optional


# 单链表定义
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        方法1: 直接遍历

        思路: 创建一个哨兵结点, 之后使用两个指针遍历需要合并的两个链表, 进行比较后选出最小值并用哨兵结点逐个连接成合并后的链表

        时间复杂度: O(m+n), m与n为两个链表的长度
        空间复杂度: O(1)

        :param list1: Optional[ListNode]
        :param list2: Optional[ListNode]
        :return: Optional[ListNode]
        """

        # 创建哨兵结点, 用于将结点统一串起来
        newHead = ListNode(-1)
        # 新链表尾插法需要的指针
        newPtr = newHead

        # 依次比较两个链表的结点值, 将较小的结点先串在newPtr指针后
        while list1 and list2:
            if list1.val <= list2.val:
                newPtr.next = list1
                list1 = list1.next
            else:
                newPtr.next = list2
                list2 = list2.next
            newPtr = newPtr.next

        # 完成上面的合并后, l1与l2最多只有一个还未被合并完, 直接将newPtr指向合并完的链表即可
        newPtr.next = list1 if list1 else list2

        # 哨兵结点不需要返回
        return newHead.next
