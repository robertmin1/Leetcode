class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1 or not head:
            return head

        # Function to reverse a part of the linked list
        def reverseLinkedList(start, end):
            prev, curr = None, start
            while curr != end:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
            return prev

        dummy = ListNode(0)
        dummy.next = head
        prev_end = dummy

        while head:
            kth = head
            # Find the kth node
            for i in range(k):
                kth = kth.next
                if not kth and i != k - 1:
                    return dummy.next  # Return if the remaining nodes are fewer than k

            # Reverse k nodes
            new_start = reverseLinkedList(head, kth)

            # Connect reversed part with the previous part
            prev_end.next = new_start
            head.next = kth
            prev_end = head
            head = kth

        return dummy.next
