# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        ans = []

        def dfs(node, i):
            if not node:
                return
            if i >= len(ans):
                ans.append([])
            ans[i].append(node.val)
            dfs(node.left, i + 1)
            dfs(node.right, i + 1)

        dfs(root, 0)
        return ans
