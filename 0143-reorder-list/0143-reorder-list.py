# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next is None:
            return
        
        def findMid(head):
            f = s = head
            while f and f.next:
                f = f.next.next
                s = s.next
            return s
        def reverse(head):
            if not head or not head.next:
                return head
            prev = None
            current = head
            nex = head.next      
            while current:
                current.next = prev
                prev =current
                current = nex
                if nex:
                    nex = nex.next
            return prev
        
        mid = findMid(head)
        head1 = head
        head2 = reverse(mid.next)
        mid.next = None
        
        while head1 is not None and head2 is not None:
            temp = head1.next
            head1.next = head2
            head1 = temp
            
            temp = head2.next
            head2.next = head1
            head2 = temp
        
        return head
                