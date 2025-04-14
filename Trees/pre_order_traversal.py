class Node:
    def __init__(self, ):
        self.val = 0
        self.left = None
        self.right = None

def pre_order_traversal(root):
    if root:
        print(root.val, end = " ")
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

# time complexity - O(n)
# space complexity - O(h)