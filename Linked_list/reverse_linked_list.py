# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    ### Iterative Solution

    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if head is None:
    #         return None
    #     if head.next is None:
    #         actual_head = head
    #         return actual_head
    #     actual_head = self.reverseList(head.next)
    #     head.next.next=head
    #     head.next = None
    #     return actual_head

    ### Recursive Solution 1

    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if head is None or head.next is None:
    #         return head
    #     p = head
    #     q, r = None, None
    #     while p is not None:
    #         r = q
    #         q = p
    #         p = p.next
    #         q.next = r
    #     return q

    ### Recursive Solution 2

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(prev, curr):
            if curr is None:
                return prev
            n = curr.next
            curr.next = prev
            return reverse(curr, n)
        return reverse(None, head)

