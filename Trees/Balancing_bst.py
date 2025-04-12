class Node:
    def __init__(self, val = 0):
        self.left = None
        self.right = None
        self.val = val
        self.h = -1


class Balanced_BST:
    def __init__(self, ):
        self.root = None
    
    def search(self, val):
        def s(root, val):
            if root is None:
                return None
            if val > root.val:
                return s(root.right, val)
            elif val < root.val:
                return s(root.left, val)
            else:
                return root
        return s(self.root, val)

    def ll_rotation(curr):
        pass
    def lr_rotation(curr):
        pass
    def rr_rotation(curr):
        pass
    def rl_rotation(curr):
        pass
    def insert(root, val):
        pass
