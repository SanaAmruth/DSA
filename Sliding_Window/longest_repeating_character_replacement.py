#

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mapping = {}
        start = 0
        end = 0
        total = 0
        cur_sum = 0
        n = len(s)
        while end<n:
            mapping[s[end]] = mapping.get(s[end], 0) + 1
            if (end - start + 1)-max(mapping.values())<=k:
                total = max(total, end - start + 1)
            else:
                while (end - start + 1)-max(mapping.values())>k:
                    mapping[s[start]] -= 1
                    start += 1
            end += 1
        return total
                    
# Time complexity - O(n)
# Space complexity - O(1)