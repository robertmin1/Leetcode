# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        curr = head
        while curr:
            res.append(curr.val)
            curr = curr.next
        res.reverse()
        
        curr = head
        for element in res:
            curr.val = element
            curr = curr.next
        
        return head
            
        
        