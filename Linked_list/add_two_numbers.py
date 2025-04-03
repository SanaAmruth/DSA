# https://neetcode.io/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        carry = 0
        while l1 is not None or l2 is not None or carry!=0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum_ = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10
            temp = ListNode(val = sum_)
            tail.next = temp
            tail = tail.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next

# time complexity - O(n)
# space complexity - O(1)