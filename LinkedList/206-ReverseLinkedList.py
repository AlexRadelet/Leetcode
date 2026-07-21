# Definition for singly-linked list.

# 2 types of solutions : recursive or iterative
#Here the iterative solution
#2 pointers, c on the first node and p before c (None at beginning)
#curr = head
#prev = None
#At first, we want the first node point to nothing to reverse
#To not lose the rest of the list, we creat tmp to store the next node
#tmp = c.next
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
# Time : O(n)
# Space : O(1)
# Better than recursive solution because it's O(n) in recursive

