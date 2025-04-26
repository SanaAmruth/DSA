# 

import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for i in tasks:
            freq[i] = freq.get(i,0) + 1
        pre = [[-freq[i],i] for i in freq]
        heapq.heapify(pre)
        queue = deque()
        time = 0
        while len(pre)!=0 or len(queue)!=0:
            if len(queue):
                if queue[0][0] < time:
                    t = queue.popleft()
                    if t[1][0] < n:
                        heapq.heappush(pre, t[1])
            if pre:
                p = heapq.heappop(pre)
                p[0] += 1
                if p[0]<0:
                    queue.append([time + n, p])
            time += 1
        return time

# time complexity - O(n*len(tasks))
# space complexity - O(n)