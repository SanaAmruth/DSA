# https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self, ):
        # self.both = [0, 0]
        self.lca = None
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def lca(root, p, q):
            if root is None:
                return None
            if root.val == p.val or root.val == q.val:
                return root
            lca1 = lca(root.left, p, q)
            lca2 = lca(root.right, p, q)
            if lca1 and lca2:
                return root
            if lca1 is not None:
                return lca1
            return lca2
        return lca(root, p, q)

# time complexity - O(n)
# space complexity - O(height of tree)