# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101)  # because range is from -100<= val <= 100
        dummy.next = head

        cur = dummy
        prev = None

        while cur.next:
            prev = cur.val
            if prev == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next
