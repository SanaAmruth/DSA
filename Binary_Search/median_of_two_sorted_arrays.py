# https://neetcode.io/problems/median-of-two-sorted-arrays

import copy
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def value(arr, idx):
            if idx < 0:
                return -sys.maxsize-1
            elif idx >= len(arr):
                return sys.maxsize
            else:
                return arr[idx]
        def find_partition(arr1, arr2, n1, n2):
            low = 0
            high = n1
            while True:
                x_par = low + (high - low)//2
                y_par = (n1+n2+1)//2 - x_par
                if value(arr1,x_par-1)<=value(arr2,y_par) and value(arr2,y_par-1)<=value(arr1,x_par):
                    return value(arr1,x_par-1), value(arr1,x_par), value(arr2,y_par-1), value(arr2,y_par)
                elif value(arr1,x_par-1)>value(arr2,y_par):
                    high = x_par - 1
                else:
                    low = x_par + 1
            return x1,x2,y1,y2
        n1 = len(nums1)
        n2 = len(nums2)
        if n1!=n2:
            arr1 = copy.deepcopy(nums1) if len(nums1)<len(nums2) else copy.deepcopy(nums2)
            arr2 = copy.deepcopy(nums2) if len(nums1)<len(nums2) else copy.deepcopy(nums1)
        else:
            arr1 = copy.deepcopy(nums1)
            arr2 = copy.deepcopy(nums2)
        x1,x2,y1,y2 = find_partition(arr1, arr2, n1, n2)
        if (n1+n2) % 2 == 0:
            return (max(x1,y1) + min(x2,y2)) / 2
        else:
            return max(x1, y1)

# time complexity - O(log(min(m,n)))
# space complexity - O(1)