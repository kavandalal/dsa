# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Recursive BFS
    # TC - O(n)
    # SC - O(height)
    def solve2(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newNode = TreeNode(val, root)
            return newNode

        q = [root]
        ct2 = 1
        while ct2 < depth-1:
            temp = []
            while q:
                popFirst = q.pop(0)
                if popFirst.left:
                    temp.append(popFirst.left)
                if popFirst.right:
                    temp.append(popFirst.right)
            ct2 += 1
            q = temp
        while q:
            node = q.pop(0)
            temp = node.left
            node.left = TreeNode(val)
            node.left.left = temp

            temp = node.right
            node.right = TreeNode(val)
            node.right.right = temp

        return root

    # Recursive DFS
    # TC - O(n)
    # SC - O(n)
    def solve1(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        ct1 = 1
        if depth == 1:
            newNode = TreeNode(val, root)
            return newNode

        def dfs(node, ct1):
            if not node:
                return
            if ct1 == depth-1:
                temp = node.left
                node.left = TreeNode(val)
                node.left.left = temp

                temp = node.right
                node.right = TreeNode(val)
                node.right.right = temp

                return
            else:
                dfs(node.left, ct1+1)
                dfs(node.right, ct1+1)

        dfs(root, ct1)
        return root
