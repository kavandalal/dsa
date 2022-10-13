# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        cur = head
        prev = None
        while cur.next:
            n = ListNode(cur.val, prev)
            prev = n
            cur = cur.next
        n = ListNode(cur.val, prev)
        prev = n
        return prev
