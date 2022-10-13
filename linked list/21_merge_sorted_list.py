# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# TC - O(n)
# SC - O(1)


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l = list1
        r = list2
        cur = head = ListNode()
        while l and r:
            if l.val < r.val:
                cur.next = l
                cur = l
                l = l.next
            else:
                cur.next = r
                cur = r
                r = r.next
        if l or r:
            cur.next = l if l else r
        return head.next
