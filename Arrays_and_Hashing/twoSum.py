from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_count = dict()
        num_idx = defaultdict(list)
        for idx, i in enumerate(nums):
            num_count[i] = num_count.get(i, 0) + 1
            num_idx[i].append(idx)
        for i in nums:
            if target - i in num_count:
                if target - i == i:
                    if num_count[i]>=2:
                        return sorted([num_idx[i][0],num_idx[i][1]])
                else:
                    return sorted([num_idx[i][0],num_idx[target-i][0]])
        return []

# time complexity O(n)
# space complexity O(n)