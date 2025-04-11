# https://neetcode.io/problems/kth-smallest-integer-in-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self, ):
        self.kth = -1
        self.arr = []
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.arr.append(root.val)
            inorder(root.right)
        inorder(root)
        return self.arr[k-1]
    
# time complexity - O(n)
# space complexity - O(h)