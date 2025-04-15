# https://neetcode.io/problems/merge-k-sorted-linked-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        counter = 0
        for i in lists:
            if i:
                counter += 1
                heapq.heappush(heap, (i.val, counter, i))
        if counter == 0:
            return None
        if counter == 1:
            return heapq.heappop(heap)[2]
        head = None
        tail = None
        while heap:
            node = heapq.heappop(heap)
            if head:
                tail.next = node[2]
                tail = tail.next
            if head is None:
                head = node[2]
                tail = head
            if tail.next:
                counter += 1
                heapq.heappush(heap, (node[2].next.val, counter, node[2].next))
        return head
            
# k linked lists
# n nodes in each linked list
# time complexity - O(klogk + (nk-k)*logk)
# space complexity - O(k)