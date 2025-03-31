# https://neetcode.io/problems/eating-bananas

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_taken(piles, speed):
            # to get the ceil of hours
            return sum([(p+speed-1)//speed for p in piles])
        n = len(piles)
        low = 1
        high = 10**9
        mid = low + (high - low)//2
        k = 10**9
        while low<=high:
            mid = low + (high - low)//2
            h_needed = hours_taken(piles, mid)
            if h_needed == h:
                k = mid
                high = mid - 1
            elif h_needed < h:
                k = mid
                high = mid - 1
            else:
                low = mid + 1
        return k
    
# time complexity - (number_of_piles)*log(10**9)
# space complexity - O(1) extra space