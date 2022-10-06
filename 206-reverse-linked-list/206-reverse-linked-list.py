# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dumlist = []

        while head:
            dumlist.append(head.val)
            head = head.next
        dumlist = reversed(dumlist)
        dummy = ListNode(0)
        head = dummy
        for num in dumlist:
            head.next = ListNode(num)
            head = head.next
        return dummy.next
            
        