# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = head
        lis = []
        while i:
            lis.append(i.val)
            i = i.next
        lis = sorted(lis)
        dummy = ListNode(0)
        ptn = dummy
        
        for num in lis:
            ptn.next = ListNode(num)
            ptn = ptn.next
        return dummy.next