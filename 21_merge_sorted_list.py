# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def show(self):
        lr = self
        while lr is not None:
            print(lr.val)
            lr = lr.next


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        if l1.val < l2.val:
            lr = l1
            l1p = l1.next
            l2p = l2
        else:
            lr = l2
            l1p = l1
            l2p = l2.next

        lrp = lr

        while True:
            lr.show()
            print("-" * 20)
            if l1p is None:
                lrp.next = l2p
                return lr

            if l2p is None:
                lrp.next = l1p
                return lr

            if l1p.val < l2p.val:
                lrp.next = l1p
                l1p = l1p.next
            else:
                lrp.next = l2p
                l2p = l2p.next

            lrp = lrp.next

        return lr

s = Solution()

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

lr = s.mergeTwoLists(l1, l2)

print("~" * 20)
lr.show()
