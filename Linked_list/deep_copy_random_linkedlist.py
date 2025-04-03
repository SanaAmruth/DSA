# https://neetcode.io/problems/copy-linked-list-with-random-pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        mapping = {}
        curr = head
        head1 = []
        while curr is not None:
            temp = Node(x = curr.val)
            mapping[curr] = mapping.get(curr, temp)
            curr = curr.next
        curr = head
        while curr:
            if curr.next:
                mapping[curr].next = mapping[curr.next]
            if curr.random is None:
                mapping[curr].random = None
            else:
                mapping[curr].random = mapping[curr.random]
            curr = curr.next
        return mapping[head]

# time complexity - O(n)
# space complexity - O(n)