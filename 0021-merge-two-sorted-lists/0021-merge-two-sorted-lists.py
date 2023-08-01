# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2) -> Optional[ListNode]:
        l1, l2 = list1, list2
        dummy = ListNode(0)
        pos = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                pos.next = l1
                l1 = l1.next
            else:
                pos.next = l2
                l2 = l2.next
            
            pos = pos.next
        
        while l1:
            pos.next = l1
            l1 = l1.next
            pos = pos.next
        
        while l2:
            pos.next = l2
            l2 = l2.next
            pos = pos.next
            
        return dummy.next