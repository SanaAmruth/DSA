# https://neetcode.io/problems/remove-node-from-end-of-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None and n == 1:
            return None
        dummy = ListNode(val = 0)
        dummy.next = head
        temp = head
        for _ in range(n):
            if temp is None:
                return head
            temp = temp.next
        
        curr = dummy
        while temp is not None:
            curr = curr.next
            temp = temp.next
        curr.next = curr.next.next
        return dummy.next

# time complexity - O(n)
# space complexity - O(1)