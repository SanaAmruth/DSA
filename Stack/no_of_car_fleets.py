# https://neetcode.io/problems/car-fleet

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        distance = [target - p for p in position]
        time = [d/v for d,v in zip(distance, speed)]
        p_t_pair = [(p, t) for p,t in zip(position, time)]
        p_t_pair.sort(key = lambda x:x[0], reverse = True)
        n = len(position)
        stack = []
        for i in range(n):
            if not stack or p_t_pair[i][1]>stack[-1]:
                stack.append(p_t_pair[i][1])
        return len(stack)

# time complexity: O(nlogn)
# space complexity: O(n)