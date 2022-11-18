# LINKS https://www.youtube.com/watch?v=CvrPf1-flAA

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        lHeight = 1
        l = root.left
        while l:
            l = l.left
            lHeight += 1

        rHeight = 1
        r = root.right
        while r:
            r = r.right
            rHeight += 1

        if lHeight == rHeight:
            return (2**lHeight) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
