# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dh = ListNode(next = head)
        fast = slow = dh.next

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        head2 = slow.next
        slow.next = None

        prev = None
        curr = head2

        # important note - we could simply temporarily hold next value
        # instead of creating an entire node and then setting next.
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head2 = prev
        count = 0
        curr = head
        while curr:
            if count % 2 == 0:
                head = head.next
                curr.next = head2
            else:
                head2 = head2.next
                curr.next = head
            curr = curr.next
            count += 1
        dh= dh.next