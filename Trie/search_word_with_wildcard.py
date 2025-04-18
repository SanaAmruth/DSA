# https://neetcode.io/problems/design-word-search-data-structure

class Node:
    def __init__(self, ):
        self.mapping = [None for _ in range(26)]
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in word:
            if curr.mapping[ord(i)-ord('a')] is None:
                curr.mapping[ord(i)-ord('a')] = Node()
            curr = curr.mapping[ord(i)-ord('a')]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def helper(curr, word, idx):
            if idx == len(word):
                return curr.is_end
            if word[idx] == '.':
                summ = []
                for i in curr.mapping:
                    if i:
                        summ.append(helper(i, word, idx + 1))
                for j in summ:
                    if j == True:
                        return True
                return False
            elif curr.mapping[ord(word[idx]) - ord('a')] is None:
                return False
            return helper(curr.mapping[ord(word[idx]) - ord('a')], word, idx + 1)
        return helper(self.root, word, 0)

