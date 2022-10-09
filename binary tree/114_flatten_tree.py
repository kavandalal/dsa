# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # TC - O(n) (faster)
    # SC - O(n)
    def solve1(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def backtrack(node):
            if not node:
                return

            backtrack(node.right)
            backtrack(node.left)

            node.right = self.prev
            node.left = None
            self.prev = node

        self.prev = None
        backtrack(root)

    # TC - O(n) (slower - as we have to traverse to right)
    # SC - O(1)
    def solve2(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root
        while cur:
            if cur.left:
                prev = cur.left
                while prev.right:
                    prev = prev.right
                prev.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right

# LINKS https://www.youtube.com/watch?v=sWf7k1x9XR4
