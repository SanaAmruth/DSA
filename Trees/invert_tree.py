# https://neetcode.io/problems/invert-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root

# time complexity - O(n)
# space complexity - O(n) --> recursion stack