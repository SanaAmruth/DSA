# https://neetcode.io/problems/longest-substring-without-duplicates

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0 or n == 1:
            return n
        mapping = {}
        start, total = 0, 1
        mapping[s[0]] = mapping.get(s[0], 0)
        n = len(s)
        curr_total = 1
        for i in range(1, n):
            if s[i] in mapping:
                if mapping[s[i]]<start:
                    curr_total += 1
                    total = max(total, curr_total)
                elif mapping[s[i]]>=start:
                    curr_total = i - mapping[s[i]]
                    total = max(total, curr_total)
                    start = mapping[s[i]] + 1
            else:
                curr_total += 1
                total = max(total, curr_total)
            mapping[s[i]] = i

        return total

# time complexity O(n)
# space complexity O(n)