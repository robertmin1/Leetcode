# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lis = []
        while head:
            lis.append(head.val)
            head = head.next
        lis = sorted(lis)
        dummy = ListNode(0)
        ptn = dummy
        
        for num in lis:
            ptn.next = ListNode(num)
            ptn = ptn.next
        return dummy.next