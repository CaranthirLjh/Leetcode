# 19. Remove Nth Node From End of List

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        for i in range(n):
            fast = fast.next
        
        slow = head
        prev = None
        while(fast):
            prev = slow
            slow = slow.next
            fast = fast.next
        
        if not prev:
            return head.next
        prev.next = slow.next
        return head