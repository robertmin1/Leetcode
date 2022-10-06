# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        s = []
        s = set(s)
        i = head
        while i:
            s.add(i)
            i = i.next
            if i in s:
                return True
        return False
        