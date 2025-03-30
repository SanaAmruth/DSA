# https://neetcode.io/problems/max-water-container

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n - 1
        max_area = 0
        while left < right:
            area = (right - left) * min(heights[right], heights[left])
            max_area = max(max_area, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area

# time complexity: O(n)
# space complexity: O(1)