# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #List to have access to it in the function height
        largest_diameter = [0]

        def height(root):
            if not root:
                return 0

            left_height = height(root.left)
            right_height = height(root.right)
            diameter = left_height + right_height

            largest_diameter[0] = max(largest_diameter[0], diameter)

            return 1 + max(left_height, right_height)

        height(root)
        return largest_diameter[0]

    # Time : O(n)
    # Space : O(h)
