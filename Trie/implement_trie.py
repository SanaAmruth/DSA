# https://neetcode.io/problems/implement-prefix-tree

class Node:
    def __init__(self, ):
        self.is_end = False
        self.mapping = [None for _ in range(26)]

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in word:
            if curr.mapping[ord(i) - ord('a')] is None:
                curr.mapping[ord(i) - ord('a')] = Node()
            curr = curr.mapping[ord(i) - ord('a')]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i in word:
            if curr.mapping[ord(i) - ord('a')] is None:
                return False
            curr = curr.mapping[ord(i) - ord('a')]
        return True if curr.is_end == True else False

    def startsWith(self, word: str) -> bool:
        curr = self.root
        for i in word:
            if curr.mapping[ord(i) - ord('a')] is None:
                return False
            curr = curr.mapping[ord(i) - ord('a')]
        return True
        
