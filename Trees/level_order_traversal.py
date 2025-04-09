# https://neetcode.io/problems/level-order-traversal-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        n = [[root.val]]
        q = deque()
        q.append(root)
        while len(q):
            arr = []
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    arr.append(node.left.val)
                    q.append(node.left)
                if node.right:
                    arr.append(node.right.val)
                    q.append(node.right)
            if len(q):
                n.append(arr)
        return n
                

# time complexity - O(n)
# space complexity - O(n)