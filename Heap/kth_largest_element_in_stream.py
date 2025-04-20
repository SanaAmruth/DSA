# https://neetcode.io/problems/kth-largest-integer-in-a-stream

import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.n_k_arr = []
        self.k_arr = []
        self.k = k
        nums.sort()
        n = len(nums)
        if n>k:
            self.n_k_arr = nums[:n-k]
            self.k_arr = nums[n-k:]
        else:
            self.k_arr = nums
        
    def add(self, val: int) -> int:
        def add_in_min_heap(val):
            heapq.heappush(self.k_arr, val)
        def add_in_max_heap(val):
            heapq.heappush(self.n_k_arr, -val)
        if len(self.k_arr) < self.k:
            add_in_min_heap(val)
            return self.k_arr[0]
        if val < self.k_arr[0]:
            add_in_max_heap(val)
        else:
            p = heapq.heappop(self.k_arr)
            heapq.heappush(self.k_arr, val)
            heapq.heappush(self.n_k_arr, p)
        return self.k_arr[0]

