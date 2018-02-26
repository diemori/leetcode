# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def generator(self, _list):
        if not _list:
            return None

        head = ListNode(_list[0])
        tail = head

        for val in _list[1:]:
            templn = ListNode(val)
            tail.next = templn
            tail = templn

        return head


    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        node_dict = dict()
        temp = head.next
        cnt = 0

        node_dict[cnt] = head

        while temp:
            cnt += 1
            node_dict[cnt] = temp
            temp = temp.next

        if cnt == n - 1:
            head = head.next
        else:
            node_dict[cnt - n].next = node_dict[cnt - n + 1].next

        return head

s = Solution()

head = s.generator([1])

result = s.removeNthFromEnd(head, 1)

while result:
    print(result.val)
    result = result.next
