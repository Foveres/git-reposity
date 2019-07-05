class ListNode:
    def __init__(self, x):      # 结点的两个属性
        self.data = x           # 节点存储的值
        self.next = None        # next默认值一般为None


class Solution(object):
    def __init__(self):
         self.length = 0
         self.head = None


    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 链表下一个元素是否需要加1,或者链表最后是否需要增加结点
        carry = 0
        res = pre = ListNode(0)     # 创建res和pre两个结点，具有共同的地址
        # 判断l1、l2、node是否有值
        while l1 or l2 or carry:
            if l1:
                carry += l1.data
                l1 = l1.next
            if l2:
                carry += l2.data
                l2 = l2.next
            carry, data = divmod(carry, 10)     # 现在carry具有同结点的和，需要判断sum是否大于10
            pre.next = ListNode(data)           # pre已经存在，创建pre.next;
            pre = pre.next                      # 进行迭代更新
        return res.next


if __name__ == '__main__':
    # 定义l1
    l1 = ListNode(2)
    l1.next = l11 = ListNode(4)         # 先创建l11:l11 = ListNode(4) 和 #将l11的地址赋给l1.next:l1.next = l11
    l11.next = l12 = ListNode(3)
    # 定义l2
    l2 = ListNode(5)
    l2.next = l21 = ListNode(6)
    l21.next = l22 = ListNode(4)
    # 创建Solution的对象
    addTwoNumbersExp = Solution()
    res = addTwoNumbersExp.addTwoNumbers(l1, l2)
    while res:
        print(res.data)
        res = res.next
