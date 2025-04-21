# https://neetcode.io/problems/last-stone-weight

import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        n = len(stones)
        heapq.heapify(stones)
        while len(stones)!=0 and len(stones)!=1:
            one = heapq.heappop(stones)
            two = heapq.heappop(stones)
            print(stones)
            if one == two:
                continue
            else:
                heapq.heappush(stones, -abs(two-one))
        return 0 if len(stones) == 0 else -stones[0]

# time complexity - O(nlogn)