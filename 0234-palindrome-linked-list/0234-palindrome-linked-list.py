# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        vals = []
        
        while curr:
            vals.append(curr.val)
            curr = curr.next

        return vals == vals[::-1]