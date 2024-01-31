# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        l = 1
        rev = []
        while curr:
            if l == left:
                present = curr
                while l <= right:
                    rev.append(present.val)
                    right-=1
                    present= present.next
                rev.reverse()
                break
            curr = curr.next
            l+=1
        
        for num in rev:
            curr.val = num
            curr = curr.next
        
        return head
                
                    