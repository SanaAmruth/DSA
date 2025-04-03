# Median of Two Sorted Arrays

This solution addresses the "Median of Two Sorted Arrays" problem, which asks to find the median of two sorted arrays.

## Problem Description

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the merged sorted array.

## Solution Explanation

The solution employs a binary search approach to find the correct partition points in the two sorted arrays.

1.  **`value(arr, idx)` Function:**
    * This helper function retrieves the value at a given index `idx` from the array `arr`.
    * It handles boundary cases by returning `negative infinity` for indices less than 0 and `positive infinity` for indices greater than or equal to the array length.

2.  **`find_partition(arr1, arr2, n1, n2)` Function:**
    * This is the core of the solution. It performs a binary search to find the correct partition points.
    * `low` and `high` represent the search space within `arr1`.
    * `x_par` and `y_par` are the partition points in `arr1` and `arr2`, respectively.
    * The `while` loop continues until the correct partition is found.
    * The condition `value(arr1, x_par - 1) <= value(arr2, y_par) and value(arr2, y_par - 1) <= value(arr1, x_par)` checks if the partitions are valid.
    * If the partitions are valid, it returns the values around the partition points (`x1`, `x2`, `y1`, `y2`).
    * If `value(arr1, x_par - 1) > value(arr2, y_par)`, the search space is narrowed by setting `high = x_par - 1`.
    * If `value(arr2, y_par - 1) > value(arr1, x_par)`, the search space is narrowed by setting `low = x_par + 1`.

3.  **`findMedianSortedArrays(nums1, nums2)` Function:**
    * The main function takes two sorted arrays `nums1` and `nums2` as input.
    * It ensures that `arr1` is the smaller array.
    * It calls `find_partition` to get the partition values.
    * If the combined length of the arrays is even, the median is the average of the maximum of the left partition values and the minimum of the right partition values.
    * If the combined length is odd, the median is the maximum of the left partition values.

## Time and Space Complexity

* **Time Complexity: O(log(min(m, n)))**
    * The binary search is performed on the smaller array, resulting in logarithmic time complexity.
* **Space Complexity: O(1)**
    * The solution uses a constant amount of extra space. The deepcopies have been removed from the optimized version of the code.