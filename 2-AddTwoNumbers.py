# https://leetcode.com/problems/add-two-numbers/
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        if self.next is None:
            return str(self.val)
        return str(self.val) + str(self.next)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        number = self.getNumber(l1) + self.getNumber(l2)
        return self.changeNumToListNode(str(number)[::-1])

    def getNumber(self, numNode: ListNode) -> int:
        # get number from node & change type from int to str & join
        return int(''.join(map(str, self.getNumberList(numNode)[::-1])))

    def getNumberList(self, node: ListNode) -> List[int]:
        if node.next:
            return [node.val] + self.getNumberList(node.next)
        else:
            return [node.val]

    def changeNumToListNode(self, num: str) -> ListNode:
        if num:
            return ListNode(int(num[0]), self.changeNumToListNode(num[1:]))
        else:
            return None

ex1_l1 = ListNode(2, ListNode(4, ListNode(3)))
ex1_l2 = ListNode(5, ListNode(6, ListNode(4)))

ex2_l1 = ListNode(5, ListNode(6))
ex2_l2 = ListNode(5, ListNode(4, ListNode(9)))

print(Solution().addTwoNumbers(ex1_l1, ex1_l2))
print(Solution().addTwoNumbers(ex2_l1, ex2_l2))
