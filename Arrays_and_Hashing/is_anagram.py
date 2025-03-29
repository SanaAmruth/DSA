# https://neetcode.io/problems/is-anagram

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
        for i in s:
            dict1[i]+=1
        for i in t:
            dict2[i]+=1
        for i in dict1.keys():
            if dict1[i]!=dict2[i]:
                return False
        for i in dict2.keys():
            if dict1[i]!=dict2[i]:
                return False
        return True

# time complexity O(4n)
# space complexity O(2n)

### better solution

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_count = dict()
        for c in s:
            char_count[c] = char_count.get(c, 0) + 1
        
        for c in t:
            if c not in char_count:
                return False
            char_count[c] -= 1
            if char_count[c] == 0:
                del char_count[c]
        
        return len(char_count) == 0

# time complexity O(2n)
# space complexity O(n)


### best solution

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)
    
# n - number of elements
# k - number of unique elements
# O(n) for counter object creation
# O(k) for counter comparison
# time complexity is O(n) + O(n) + O(k) = O(2n + k)
# the space complexity is O(k)