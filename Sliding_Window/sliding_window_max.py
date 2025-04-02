# https://neetcode.io/problems/sliding-window-maximum

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        for idx, i in enumerate(nums[:k]):
            if len(dq) == 0 or dq[-1][1]>=i:
                dq.append([idx, i])
            else:
                while dq and dq[-1][1]<i:
                    dq.pop()
                dq.append([idx, i])
 
        window_max = [dq[0][1]]
        for i in range(k, len(nums)):
            while len(dq) != 0 and dq[0][0] < i - k + 1:
                dq.popleft()
            while len(dq)!=0 and dq[-1][1]<nums[i]:
                dq.pop()
            dq.append([i, nums[i]])
            window_max.append(dq[0][1])
        return window_max

# time complexity O(n)
# space complexity O(n)