# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        current = head

        while (current):
            stack.append(current)
            current = current.next

        if (n == len(stack)):
            return head.next
        else:
            stack[-n - 1].next = stack[-n].next
            return head