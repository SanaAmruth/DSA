# https://neetcode.io/problems/three-integer-sum

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        return_list = []
        for i in range(n-2):
            if (i > 0 and nums[i] != nums[i-1]) or i==0:
                left = i + 1
                right = n - 1
                while left < right:
                    total = nums[i] + nums[left] + nums[right]
                    if total < 0:
                        left += 1
                    elif total > 0:
                        right -= 1
                    else:
                        return_list.append([nums[i], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
        return return_list

# time complexity: O(n^2)
# space complexity: O(1)