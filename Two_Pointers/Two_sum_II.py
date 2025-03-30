# https://neetcode.io/problems/two-integer-sum-ii

from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        start = 0
        end = n - 1
        while start < end:
            if numbers[start] + numbers[end] == target:
                return [start+1, end+1]
            elif numbers[start] + numbers[end] < target:
                start += 1
            else:
                end -= 1