# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        current = head

        while (current):
            stack.append(current)
            current = current.next

        left, right = 0, len(stack) - 1
        while left < right:
            stack[left].next = stack[right]
            left += 1
            if left == right:
                break
            stack[right].next = stack[left]
            right -= 1
        
        stack[left].next = None

        