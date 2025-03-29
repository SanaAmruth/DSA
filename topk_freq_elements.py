# https://neetcode.io/problems/top-k-elements-in-list

# from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        sorted_items = sorted(freq.items(), key = lambda x: x[1], reverse = True)
        return [x[0] for x in sorted_items[:k]]

# time complexity: O(n log n) due to sorting
# space complexity: O(n) for the frequency dictionary

# Alternative solution using Counter
from collections import Counter
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return [item for item, _ in count.most_common(k)]
# time complexity: O(n log n) due to most_common
# space complexity: O(n) for the Counter object