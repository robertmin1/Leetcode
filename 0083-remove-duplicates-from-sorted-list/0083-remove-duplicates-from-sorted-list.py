# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: [ListNode]) -> [ListNode]:
        dummylist = []
        while head:
            dummylist.append(head.val)
            head = head.next

        dummylist = sorted(set(dummylist))
        dummy = ListNode(0)
        head = dummy

        for num in dummylist:
            head.next = ListNode(num)
            head = head.next
        
        return dummy.next
