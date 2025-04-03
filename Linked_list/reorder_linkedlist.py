# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def printing(head):
            curr = head
            while curr is not None:
                print(curr.val)
                curr = curr.next
            print("\n"*3)
            return
        if head is None or head.next is None:
            return None
        def find_middle(head):
            slow = fast = head
            prev = None
            while fast is not None and slow is not None and fast.next is not None:
                prev = slow
                fast = fast.next.next
                slow = slow.next
            return slow, prev
        def reverse(head):
            p, q, r = head, None, None
            while p is not None:
                r = q
                q = p
                p = p.next
                q.next = r
            return q
        middle_node, prev = find_middle(head)
        prev.next = None
        list1 = head
        list2 = reverse(middle_node)
        tail = list1
        a = list1.next
        b = list2
        while a is not None and b is not None:
            tail.next = b
            tail = b
            b = b.next
            tail.next = a
            tail = a
            a = a.next
        if a is None:
            tail.next = b
        return None

# time complexity - O(n)
# space complexity - O(1)