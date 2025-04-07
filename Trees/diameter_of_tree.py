# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.diam = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def call(root):
            if root is None:
                return 0
            lh = call(root.left)
            rh = call(root.right)
            self.diam = max(self.diam, lh + rh + 1)
            return max(lh, rh) + 1
        call(root)
        return self.diam - 1

# time complexity - O(n)
# space complexity - O(height of tree) --> due to recursion stack