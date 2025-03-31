# https://neetcode.io/problems/find-minimum-in-rotated-sorted-array
import sys
from typing import List
class Solution:
    # def mod_search(nums):
    def findMin(self, arr: List[int]) -> int:
        n = len(arr)
        low = 0
        high = n - 1
        k = sys.maxsize
        while(low<=high):
            mid = low + (high - low)//2
            if arr[low]<=arr[mid] and arr[mid]<=arr[high]:
                return arr[low]
            elif arr[mid]<arr[low]:
                k = min(k, arr[mid])
                high = mid
            else:
                low = mid + 1
        return k

# time complexity - O(logn)
# space complexity - O(1)