# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        ans = []

        def dfs(node, curList, curSum):
            if not node:
                return

            if curSum == node.val and not node.right and not node.left:
                curList += [node.val]
                ans.append(curList.copy())
                return

            left = dfs(node.left, curList + [node.val], curSum-node.val)
            right = dfs(node.right, curList + [node.val], curSum-node.val)

        dfs(root, [], targetSum)
        return ans
