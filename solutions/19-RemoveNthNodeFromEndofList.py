# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if self.next is None:
            return f"{self.val}"
        return f"{self.val} -> {self.next} "


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        head_pointer = ListNode(next=head)
        length = 0
        node = cur = head_pointer
        while True:
            length += 1
            cur = cur.next
            if length > n + 1:
                node = node.next

            if cur == None:
                if node.next is not None:
                    node.next = node.next.next
                    return head_pointer.next
                else:
                    return None


cases = [
    [ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2],
    [ListNode(1, ListNode(2)), 2],
    [ListNode(1), 1],
]

for case in cases:
    print(Solution().removeNthFromEnd(*case))
