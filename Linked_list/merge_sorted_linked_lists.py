# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val > list2.val:
            temp = list1
            list1 = list2
            list2 = temp
        head = tail = list1
        a = list1.next
        b = list2
        while a is not None and b is not None:
            if a.val<b.val:
                tail.next = a
                tail = a
                a = a.next
            else:
                tail.next = b
                tail = b
                b = b.next
        if a is None:
            tail.next = b
        if b is None:
            tail.next = a
        return head
