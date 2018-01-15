# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def show(self):
        print(self.val)
        next = self.next

        while next is not None:
            print(next.val)
            next = next.next


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lt1 = l1
        lt2 = l2
        lr = None
        upper = 0

        while lt1 is not None or lt2 is not None:
            if lt1 is not None:
                val1 = lt1.val
                lt1 = lt1.next
            else:
                val1 = 0

            if lt2 is not None:
                val2 = lt2.val
                lt2 = lt2.next
            else:
                val2 = 0

            temp_sum = val1 + val2 + upper
            stay = temp_sum % 10

            if lr is None:
                lr = ListNode(stay)
                lrt = lr
            else:
                lrt.next = ListNode(stay)
                lrt = lrt.next

            upper = temp_sum // 10

        if upper > 0:
            lrt.next = ListNode(upper)

        return lr


ln1 = ListNode(5)
# ln1.next = ListNode(2)
# ln1.next.next = ListNode(3)

ln2 = ListNode(5)
# ln2.next = ListNode(5)
# ln2.next.next = ListNode(5)

s = Solution()

lr = s.addTwoNumbers(ln1, ln2)

lr.show()
