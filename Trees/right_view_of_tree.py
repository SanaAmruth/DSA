# 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self, ):
        self.ret = []
        self.v = {}
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def rev_pre_order(root, v, m = -1):
            if root is None:
                return
            if v>m and v not in self.v:
                self.ret.append(root.val)
                self.v[v] = root
            m = max(m, v)
            rev_pre_order(root.right, v + 1, m)
            rev_pre_order(root.left, v + 1, m)
        rev_pre_order(root, 0, -1)
        return self.ret

# time complexity - O(n)
# space complexity - O(height of tree)