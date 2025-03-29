# https://neetcode.io/problems/longest-consecutive-sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_map = {}
        for i in nums:
            nums_map[i] = nums_map.get(i,0) + 1
        max_val = 1
        for key in nums_map:
            # use only potential start of consecutive sequence
            if key - 1 not in nums_map:
                cons = 1
                while key+1 in nums_map:
                    cons += 1
                    key += 1
                max_val = max(cons, max_val)
        return max_val

# time complexity: O(n)
# space complexity: O(n)