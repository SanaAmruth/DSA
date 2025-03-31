#

import bisect
class TimeMap:

    def __init__(self):
        self.mapping = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapping[key]= self.mapping.get(key, {})
        self.mapping[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        def first_greater_element(arr, target):
            n = len(arr)
            low = 0
            high = n - 1

            while low <= high:
                mid = low + (high - low) // 2
                if arr[mid] <= target:
                    low = mid + 1
                else:
                    high = mid - 1
            return low 
        if key not in self.mapping:
            return ""
        timestamps = sorted(list(self.mapping[key].keys()))
        idx = first_greater_element(timestamps, timestamp)
        if idx == 0:
            return ""
        return self.mapping[key][timestamps[idx - 1]]
