# https://neetcode.io/problems/subtree-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return subRoot is None
        def isSame(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val!=q.val:
                return False
            return isSame(p.left, q.left) and isSame(p.right, q.right)
        if isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

# time complexity - O(n)
# time complexity - O(n)