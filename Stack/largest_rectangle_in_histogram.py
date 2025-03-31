# https://neetcode.io/problems/largest-rectangle-in-histogram

class Solution:
    def next_smaller_element(self, heights):
        stack = []
        mapping = {}
        n = len(heights)
        for idx, i in enumerate(heights):
            if len(stack)==0 or i>=stack[-1][1]:
                stack.append([idx,i])
            else:
                while len(stack)>0 and i<stack[-1][1]:
                    mapping[stack[-1][0]] = mapping.get(stack[-1][0], idx)
                    stack.pop()
                stack.append([idx,i])
        while len(stack)>0:
            mapping[stack[-1][0]] = mapping.get(stack[-1][0], n)
            stack.pop()
        stack = []
        for i in range(n):
            stack.append(mapping[i])
        return stack

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        suffix_next_smaller = self.next_smaller_element(heights)
        prefix_next_smaller = [n-1-t for t in self.next_smaller_element(heights[::-1])][::-1]
        max_area = heights[0]
        for i in range(n):
            area = heights[i]*(suffix_next_smaller[i]-prefix_next_smaller[i]-1)
            max_area = max(area, max_area)
        return max_area

# Time Complexity: O(n)
# Space Complexity: O(n)