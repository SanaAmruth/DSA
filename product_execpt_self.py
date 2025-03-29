# https://neetcode.io/problems/products-of-array-discluding-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] * nums[i-1])
        nums_rev = nums[::-1]

        suffix = [1]
        for i in range(1, len(nums_rev)):
            suffix.append(suffix[-1] * nums_rev[i-1])
        suffix = suffix[::-1]
        return [i*j for (i,j) in zip(prefix, suffix)]

# time complexity: O(n)
# space complexity: O(n)