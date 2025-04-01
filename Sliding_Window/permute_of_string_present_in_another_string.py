# https://neetcode.io/problems/permutation-string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        d1 = [0] * 26
        d2 = [0] * 26
        
        for i in range(len(s1)):
            d1[ord(s1[i])-ord('a')] += 1
            d2[ord(s2[i])-ord('a')] += 1
            
        if d1 == d2: return True
        
        for i in range(1, len(s2)-len(s1)+1):
            d2[ord(s2[i-1])-ord('a')] -= 1
            d2[ord(s2[i+len(s1)-1])-ord('a')] += 1
            if d1 == d2: return True
            
        return False