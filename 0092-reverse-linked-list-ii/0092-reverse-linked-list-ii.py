# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l = 1
        current = head
        prev = None
        
        while l != left:
            prev = current
            current = current.next
            l+=1

        Start = prev
        NewEnd = current
        nex = current.next
        
        for num in range(right-left+1):
            current.next = prev
            prev = current
            current = nex
            if nex:
                nex = nex.next
        
        if Start:
            Start.next = prev
        else:
            head = prev
            
        NewEnd.next = current
        
        return head
        