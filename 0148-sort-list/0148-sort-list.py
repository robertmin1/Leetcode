# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        tempHead= head
        while(tempHead):
            arr.append(tempHead.val)
            tempHead = tempHead.next
        arr.sort()
        tempHead= head
        for elem in arr:
            tempHead.val =elem
            tempHead = tempHead.next
        return head
        