# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # recurssion || dfs, better than 2 pointer
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nodes = set()

        def dfs(node):
            if not node:
                return False

            if node.val in nodes:
                nodes.remove(node.val)
                return True

            nodes.add(k - node.val)
            left = dfs(node.left)
            if left:
                return True

            nodes.add(k - node.val)
            right = dfs(node.right)
            if right:
                return True

            return False
        return dfs(root)

    # 2 pointer , dfs is better
    def solve2(self, root: Optional[TreeNode], k: int) -> bool:
        a = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            a.append(node.val)
            inorder(node.right)
        inorder(root)

        left = 0
        right = len(a) - 1
        while left < right:
            sumHere = a[left] + a[right]
            if sumHere == k:
                return True
            elif sumHere < k:
                left += 1
            else:
                right -= 1
        return False
