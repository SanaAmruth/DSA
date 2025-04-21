# https://neetcode.io/problems/k-closest-points-to-origin

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        arr = points[:k]
        dist = lambda x: -(x[0]*x[0] + x[1]*x[1])
        arr = [[dist(i),idx,i] for idx, i in enumerate(points[:k])]
        heapq.heapify(arr)
        if n>k:
            count = k
            for idx, i in enumerate(points[k:]):
                count += 1
                if -dist(i) < -arr[0][0]:
                    heapq.heappop(arr)
                    heapq.heappush(arr, [dist(i),idx + k,i])
        return [i[2] for i in arr]

# time complexity - O(nlogk)
# space complexity - O(k)