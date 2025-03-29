# https://neetcode.io/problems/anagram-groups

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            freq = [0]*(ord('z')-ord('A'))
            for char in word:
                freq[ord(char)-ord('A')] += 1
            freq = tuple(freq)
            anagrams[freq].append(word)
        return anagrams.values()