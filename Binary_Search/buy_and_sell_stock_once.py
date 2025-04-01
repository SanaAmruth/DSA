# https://neetcode.io/problems/buy-and-sell-crypto

class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        p = arr[::-1]
        prefix_high = [p[0]]
        n = len(arr)
        for i in range(1, n):
            prefix_high.append(max(p[i], prefix_high[-1]))
        suffix_high = prefix_high[::-1]
        profit = 0
        for i in range(n):
            profit = max(profit, suffix_high[i]-arr[i])
        return profit

# time complexity - O(n)
# space complexity - O(n) --> it can be reduced to O(1)