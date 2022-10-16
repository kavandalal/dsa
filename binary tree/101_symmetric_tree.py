# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(l, r):
            if not l and not r:
                return True

            if not l or not r:
                return False

            if l.val == r.val:
                return dfs(l.left, r.right) and dfs(l.right, r.left)

            return False

        return dfs(root.left, root.right)
