# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return
        
        prev = None
        present = head
        nex = head.next
        
        while present:
            present.next = prev
            prev = present
            present = nex
            if nex:
                nex = nex.next
            
            
        return prev
            
        
        