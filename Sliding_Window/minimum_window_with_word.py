# https://neetcode.io/problems/minimum-window-with-characters

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def greater(d1, d2):
            if len(set(d2.keys()) - set(d1.keys())) > 0:
                return False
            for i in d2:
                if d1[i]<d2[i]:
                    return False
            return True
        d1 = {}
        d2 = {}
        for i in t:
            d2[i] = d2.get(i,0) + 1
        for i in s:
            d1[i] = d1.get(i,0) + 1
        if greater(d1, d2) == False:
            return ""
        start = 0
        end = len(s) - 1
        while greater(d1,d2):
            d1[s[start]] -= 1
            start += 1
        start -= 1
        d1[s[start]] += 1
        while greater(d1,d2):
            d1[s[end]] -= 1
            end -= 1
        end += 1
        d1[s[end]] += 1
        return s[start:end+1]

# time complexity - O(n)
# space complexity - O(distinct_no_of_characters)