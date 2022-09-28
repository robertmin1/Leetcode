# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        lis = []
        for i in lists:
            while i:
                lis.append(i.val)
                i = i.next
        lis = sorted(lis)
        print(lis)
        dummy = ListNode(0)
        head = dummy
        for num in lis:
            head.next = ListNode(num)
            head = head.next
        return dummy.next
        