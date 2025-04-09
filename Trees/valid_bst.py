# https://neetcode.io/problems/valid-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self, ):
        self.arr = []
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(root):
            if root is not None:
                inorder(root.left)
                self.arr.append(root.val)
                inorder(root.right)
            
        def is_sorted(arr):
            for i in range(len(arr)-1):
                if arr[i]>=arr[i+1]:
                    return False
            return True

        inorder(root)
        return is_sorted(self.arr)

# time complexity - 
# space complexity - 