class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def findMid(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, head):
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev

    def reorderList(self, head):
        if not head or not head.next or self.hasCycle(head):
            return

        mid = self.findMid(head)
        head1 = head
        head2 = self.reverse(mid.next)
        mid.next = None

        while head1 and head2:
            temp1, temp2 = head1.next, head2.next
            head1.next = head2
            head2.next = temp1
            head1, head2 = temp1, temp2

# Example usage
# list_head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
# Solution().reorderList(list_head)
# while list_head:
#     print(list_head.val)
#     list_head = list_head.next
