# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        slow = fast = head
        while fast.next and fast.next.next:
            cur = slow
            slow = slow.next
            fast = fast.next.next

        if fast.next:
            cur = slow
        cur.next = cur.next.next
        return dummy.next
