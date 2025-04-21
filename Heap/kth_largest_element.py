# https://neetcode.io/problems/kth-largest-element-in-an-array

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = nums[:k]
        heapq.heapify(arr)
        for val in nums[k:]:
            if val>arr[0]:
                heapq.heappop(arr)
                heapq.heappush(arr, val)
        return arr[0]

# time complexity - O(nlogk)
# space complexity - O(k)