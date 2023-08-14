from Solution1 import ListNode
from Solution1 import Solution1
from Solution2 import Solution2


# 尾插法插入新结点
def addNode(head, val):
    newNode = ListNode(val)
    ptr = head
    while ptr.next is not None:
        ptr = ptr.next
    ptr.next = newNode


# 打印链表, 箭头形式
def printNodeArrow(head):
    ptr = head
    while ptr is not None:
        print(ptr.val, end=" -> ")
        ptr = ptr.next
    print("None")


# 打印链表, 列表形式
def printNodeList(head):
    ptr = head
    print("[", end="")
    if ptr is not None:
        while ptr.next is not None:
            print("{}, ".format(ptr.val), end="")
            ptr = ptr.next
        print("{}]".format(ptr.val), end="")
    else:
        print("]", end="")


def main():
    # 准备输入信息
    valList1, lenList1 = [[1, 2, 4], [-200], [-200]], [3, 1, 1]
    valList2, lenList2 = [[1, 3, 4], [-200], [0]], [3, 1, 1]
    list1, list2 = ListNode(-1), ListNode(-1)
    for _, valList in enumerate(valList1):
        for _, val in enumerate(valList):
            addNode(list1, val)
    for i, valList in enumerate(valList2):
        for j, val in enumerate(valList):
            addNode(list2, val)

    # 准备期望输出信息
    output = [[1, 1, 2, 3, 4, 4], [], [0]]

    # 选择解决方法
    # solution = Solution1()
    solution = Solution2()

    ptr1, ptr2 = list1.next, list2.next
    for i in range(len(lenList1)):
        # 准备需要传入的两个链表l1, l2
        l1Len, l2Len = lenList1[i], lenList2[i]
        l1, l2 = ListNode(), ListNode()
        j = k = 0
        while j < l1Len:
            if ptr1.val != -200:
                addNode(l1, ptr1.val)
            ptr1 = ptr1.next
            j += 1
        while k < l2Len:
            if ptr2.val != -200:
                addNode(l2, ptr2.val)
            ptr2 = ptr2.next
            k += 1

        # 打印示例序号
        print("示例{}: ".format(i + 1))

        # 打印输入信息
        print("  输入: l1 = ", end="")
        printNodeList(l1.next)
        print(", l2 = ", end="")
        printNodeList(l2.next)
        print()

        # 打印期望输出信息
        print("  期望输出: {}".format(output[i]))

        # 打印实际输出信息
        print("  实际输出: ", end="")
        newList = solution.mergeTwoLists(l1.next, l2.next)
        printNodeList(newList)
        print(end="\n\n")


if __name__ == '__main__':
    main()
