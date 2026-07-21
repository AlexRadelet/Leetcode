# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 2 pointers : s for slow and f for fast (f move2 steps every time s move1)
#If f out of bounds, false there is no cycle
#If there is a cycle, there are pointing on the same node
#There is a guarantee they will superpose on one node
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True
        return False

# Time : O(n)
# Space : O(1) ( Hashmap will be O(n))





