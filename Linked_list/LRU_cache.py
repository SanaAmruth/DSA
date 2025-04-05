class Node:
    def __init__(self, val = 0, key = 0):
        self.val = val
        self.left = None
        self.right = None
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.mapping = {}
        self.head = Node(0,-1)
        self.tail = Node(0,-2)
        self.head.right = self.tail
        self.tail.left = self.head
        self.cap = capacity
        self.count = 0
    
    def _insert_in_front(self, node):
        one = self.head
        two = self.head.right
        node.right = two
        node.left = one
        two.left = node
        one.right = node

    def _remove_node(self, node):
        one = node.left
        two = node.right
        one.right = two
        two.left = one
        node.left = None
        node.right = None
        return node

    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1
        node = self.mapping[key]
        self._remove_node(node)
        self._insert_in_front(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            node = self.mapping[key]
            node.val = value
            self._remove_node(node)
            self._insert_in_front(node)
        else:
            node = Node(value, key)
            self.mapping[key] = node
            self._insert_in_front(node)
            self.count += 1
            if self.count > self.cap:
                removed = self._remove_node(self.tail.left)
                del self.mapping[removed.key]
                self.count -= 1
            
        return None

# - time complexity 
    # - insertion --> O(1)
    # - deletion --> O(1)
    # - search --> O(1)

# - Space complexity - O(n)