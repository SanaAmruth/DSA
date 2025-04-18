# https://neetcode.io/problems/binary-tree-maximum-path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self, ):
        self.mapping = {}
        self.maxi = -sys.maxsize-1
        # self.mapping[None]
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def value(root):
            if root:
                return root.val
            return 0
        def ite(root):
            if root:
                ite(root.left)
                ite(root.right)
                left_sum = self.mapping[root.left] if root.left else 0
                right_sum = self.mapping[root.right] if root.right else 0
                self.maxi = max(root.val + left_sum + right_sum, self.maxi)
        def func(root):
            if root is None:
                return 0
            maxi = 0
            if root.left:
                self.mapping[root.left] = max(0,func(root.left))
                maxi = max(self.mapping[root.left], maxi)
            if root.right:
                self.mapping[root.right] = max(0, func(root.right))
                maxi = max(self.mapping[root.right], maxi)
            self.mapping[root] = max(0, root.val + maxi)
            return root.val + maxi
        func(root)
        ite(root)
        return self.maxi
            
        
# time complexity - O(n)
# space complexity - O(n)