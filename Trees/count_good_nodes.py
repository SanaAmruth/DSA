# https://neetcode.io/problems/count-good-nodes-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self, ):
        self.ret = 0
    def goodNodes(self, root: TreeNode) -> int:
        def traverse(node, ma):
            if not node:
                return
            if node.val>=ma:
                self.ret += 1
            ma = max(node.val, ma)
            traverse(node.left, ma)
            traverse(node.right, ma)

        traverse(root, -sys.maxsize-1)
        return self.ret

# time complexity - O(n)
# space complexity - O(h)