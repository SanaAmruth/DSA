# https://neetcode.io/problems/daily-temperatures

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # next greater element problem
        mapping = {}
        stack = []
        n = len(temperatures)
        for idx, i in enumerate(temperatures):
            if not stack:
                stack.append([i, idx])
            else:
                if i<=stack[-1][0]:
                    stack.append([i, idx])
                else:
                    while(stack and i>stack[-1][0]):
                        mapping[stack[-1][1]] = mapping.get(stack[-1][1], idx)
                        stack.pop()
                    stack.append([i, idx])
        while stack:
            mapping[stack[-1][1]] = mapping.get(stack[-1][1], 0)
            stack.pop()
        final = [0 for _ in range(n)]
        for i in range(n):
            final[i] = max(0, mapping[i] - i)
        return final

# Time Complexity: O(n)
# Space Complexity: O(n)