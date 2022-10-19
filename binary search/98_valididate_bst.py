# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode], lessThan=float('inf'), greaterThan=float('-inf')) -> bool:

        if not root:
            return True

        if root.val >= lessThan or root.val <= greaterThan:
            return False

        x = self.isValidBST(root.left, min(lessThan, root.val), greaterThan)
        y = self.isValidBST(root.right, lessThan, max(greaterThan, root.val))
        return x and y
