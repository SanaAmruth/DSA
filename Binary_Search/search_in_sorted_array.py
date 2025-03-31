# https://neetcode.io/problems/binary-search

class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        def search_ele(low, high):
            while low<=high:
                mid = low + (high-low)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1
        return search_ele(0, len(nums)-1)