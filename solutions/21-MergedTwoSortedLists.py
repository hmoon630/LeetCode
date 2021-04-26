# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if self.next is None:
            return str(self.val)
        return str(self.val) + " " + str(self.next)


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        cur = head
        while l1 and l2:
            left, right = l1.val, l2.val

            if left < right:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next

        if l1 is None:
            cur.next = l2
        else:
            cur.next = l1

        return head.next


cases = [[ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4)))]]

for case in cases:
    print(str(Solution().mergeTwoLists(*case)))
