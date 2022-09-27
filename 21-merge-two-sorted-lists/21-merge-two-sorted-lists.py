# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list = []
        while list1 or list2:
            list.append(list1.val) if list1 else None
            list.append(list2.val) if list2 else None
            list2 = list2.next if list2 else None
            list1 = list1.next if list1 else None
        list = sorted(list)
        dummy = ListNode(0)
        itr = dummy
        for i in list:
            itr.next = ListNode(i)
            itr = itr.next
            
        return dummy.next