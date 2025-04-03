# https://neetcode.io/problems/find-duplicate-integer

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            if nums[abs(i)] < 0:
                return abs(i)
            nums[abs(i)] = -nums[abs(i)]

# time complexity - O(n)
# space complexity - O(1)