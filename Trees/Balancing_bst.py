class Node:
    def __init__(self, val = 0):
        self.left = None
        self.right = None
        self.val = val
        self.h = 1

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

    def height(self, root):
        if root is None:
            return 0
        return root.h
    
    def inorder_traversal(self, ):
        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            print(root.val)
            inorder(root.right)
        inorder(self.root)

    def update_height(self, root):
        root.h = max(self.height(root.left), self.height(root.right)) + 1

    def get_balance(self, root):
        return self.height(root.left) - self.height(root.right)

    def rotate_left(self, curr):
        A = curr
        B = curr.right
        C = curr.right.left

        B.left = A
        A.right = C
        
        return B

    def rotate_right(self, curr):
        A = curr
        B = curr.left
        C = curr.left.right

        B.right = A
        A.left = C

        return B

    def insert(self, root, val):
        if root is None:
            return Node(val)
        
        if val > root.val:
            root.right = self.insert(root.right, val)
        else:
            root.left = self.insert(root.left, val)
        
        self.update_height(root)

        balance = self.get_balance(root)


        if balance > 1:
            # left left case
            if self.get_balance(root.left) >= 0:
                return self.rotate_right(root)
            # left right case
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
        
        if balance < -1:
            # right left case
            if self.get_balance(root.right) >= 0:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)
            # right right case
            else:
                return self.rotate_left(root)
        return root


if __name__ == "__main__":
    bst = Balanced_BST()
    bst.root = bst.insert(bst.root, 1)
    bst.root = bst.insert(bst.root, 2)
    bst.root = bst.insert(bst.root, 3)
    bst.inorder_traversal()
    # print(bst.root.val)
    # print("2")
    # return