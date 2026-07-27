# Definition for a binary tree node.
from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS ! => using a Queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque()
        queue.append(root)
        ans = []

        while queue:
            level = []
            # n : number of nodes in the level
            n = len(queue)
            for i in range(n):
                # We pop from the left because it's a queue (FIFO)
                node = queue.popleft()
                level.append(node.val)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.append(level)
        return ans

    # Time : O(n)
    # Space : O(n)

