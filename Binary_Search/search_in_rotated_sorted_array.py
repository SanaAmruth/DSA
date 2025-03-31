# https://neetcode.io/problems/find-target-in-rotated-sorted-array

class Solution:
    def search(self, arr: List[int], target: int) -> int:
        n = len(arr)
        low = 0
        high = n-1
        while low<=high:
            mid = low + (high - low)//2
            if arr[mid] == target:
                return mid
            elif arr[low]<=arr[mid]:
                if target<=arr[mid] and target>=arr[low]:
                    high = mid
                else:
                    low = mid + 1
            else:
                if target>=arr[mid] and target<=arr[high]:
                    low = mid
                else:
                    high = mid - 1
        return -1

# time complexity - O(logn)
# space complexity - O(1)