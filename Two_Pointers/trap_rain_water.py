# https://neetcode.io/problems/trapping-rain-water

class Solution:
    def trap(self, heights: List[int]) -> int:
        left_max = [-sys.maxsize-1]
        n = len(heights)
        for i in range(1, n):
            left_max.append(max(heights[i-1], left_max[-1]))
        hrev = heights[::-1]
        right_max = [-sys.maxsize-1]
        for i in range(1, n):
            right_max.append(max(hrev[i-1], right_max[-1]))
        right_max.reverse()
        total = 0
        for i in range(1, n-1):
            if heights[i] < left_max[i] and heights[i] < right_max[i]:
                total += min(left_max[i],right_max[i]) - heights[i]
        return total

# Time Complexity: O(n)
# Space Complexity: O(n)