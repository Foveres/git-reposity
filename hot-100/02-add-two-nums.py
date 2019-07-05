# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

    def print_node(self):
        print(self.val)


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 新建一个ListNode：值都是0
        head = ret = ListNode(0)

        # 当l1 和 l2不为空时（或不等于0）
        while l1 and l2:
            # ret的指针指向l1与l2的和值
            ret.next = ListNode(l1.val + l2.val)
            # l1指向下一个值
            l1 = l1.next
            # l2指向下一个值
            l2 = l2.next
            # ret还是0.节点指向下一个节点
            ret = ret.next

        # 当l2位数小于l1时
        while l1:
            ret.next = ListNode(l1.val)
            l1 = l1.next
            ret = ret.next

        # 当l1位数小于l2时
        while l2:
            ret.next = ListNode(l2.val)
            l2 = l2.next
            ret = ret.next

        # 处理进位
        ret = head = head.next
        while head:
            if head.val > 9:
                if head.next == None:
                    head.next = ListNode(0)
                head.next.val += int(head.val / 10)     # 进位
                head.val %= 10                          # 当前位置的数
            head = head.next
        print(ret)
        return ret                                      # 返回第一个位置的数


if __name__ == '__main__':

    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    # l1.print_node()


    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    # l2.print_node()

    solution = Solution()
    l3 = solution.addTwoNumbers(l1, l2)

    l3.print_node()
    l3.next.print_node()
    l3.next.next.print_node()