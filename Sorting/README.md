# Sorting Algorithms Summary

This document provides an overview of common sorting algorithms, including their time and space complexities, best/worst/average cases, memory usage, cache friendliness, whether they are in-place or not, and any additional comments.

---

| **Algorithm**    | **Best Case**      | **Worst Case**    | **Average Case**  | **Time Complexity**     | **Space Complexity**   | **In-Place**   | **Memory Usage**     | **Cache Friendliness**  | **Comments** |
|------------------|--------------------|-------------------|-------------------|-------------------------|------------------------|----------------|----------------------|-------------------------|--------------|
| **Bubble Sort**  | O(n)               | O(n²)             | O(n²)             | Best: O(n), Worst: O(n²) | O(1)                   | Yes            | Very low             | Poor                    | Rarely used due to inefficiency. |
| **Selection Sort**| O(n²)              | O(n²)             | O(n²)             | O(n²)                    | O(1)                   | Yes            | Low                  | Poor                    | Inefficient for large datasets. |
| **Insertion Sort**| O(n)               | O(n²)             | O(n²)             | O(n²)                    | O(1)                   | Yes            | Very low             | Good                    | Efficient for small datasets or partially sorted data. |
| **Merge Sort**   | O(n log n)         | O(n log n)        | O(n log n)        | O(n log n)               | O(n)                   | No             | Requires extra space | Moderate                | Stable and works well with external sorting for large datasets. |
| **Quick Sort**   | O(n log n)         | O(n²)             | O(n log n)        | O(n log n)               | O(log n)               | Yes            | Low (recursive stack)| Good (if pivot optimized) | Often faster than merge sort in practice. |
| **Heap Sort**    | O(n log n)         | O(n log n)        | O(n log n)        | O(n log n)               | O(1)                   | Yes            | Very low             | Moderate                | Has guaranteed O(n log n), but often slower than Quick Sort. |
| **Radix Sort**   | O(nk)              | O(nk)             | O(nk)             | O(nk)                    | O(n+k)                 | No             | Requires extra space | Good                    | Efficient for large numbers or strings. |
| **Bucket Sort**  | O(n+k)             | O(n²)             | O(n+k)            | O(n+k)                   | O(n+k)                 | No             | Requires extra space | Good                    | Best for uniformly distributed data. |
| **Cycle Sort**   | O(n²)              | O(n²)             | O(n²)             | O(n²)                    | O(1)                   | Yes            | Low                  | Good                    | Works well with distinct elements, minimal writes. |

---

## Key Points:

- **In-Place Sorting:** Algorithms that modify the original array without using extra space are considered in-place, such as Quick Sort, Merge Sort, Heap Sort, and Insertion Sort.
- **Best for Large Data:** Merge Sort and Quick Sort (with optimized pivoting) are ideal for large datasets.
- **Stable Sorting:** Merge Sort and Insertion Sort are stable, meaning equal elements retain their relative order.
- **Space Efficient:** Insertion Sort, Selection Sort, and Quick Sort (with in-place partitioning) are more space-efficient compared to Merge Sort.
  
## Conclusion:

- **Selection Sort** and **Insertion Sort** are simple but inefficient for large datasets.
- **Quick Sort** is typically the fastest in practice, despite having a worst-case complexity of O(n²).
- **Merge Sort** is a stable and reliable choice with O(n log n) time complexity, making it suitable for large datasets or when external sorting is needed.
- **Heap Sort** offers O(n log n) performance, though it may be slower in practice due to extra overhead.
- **Radix Sort** and **Bucket Sort** are efficient for specific use cases such as sorting large integers or uniformly distributed data.
- **Cycle Sort** is efficient for cases where we want to minimize writes, especially for distinct elements, but it may not perform well with duplicate elements.

---

This document provides an overview of sorting algorithms. Depending on the size and nature of the data (e.g., nearly sorted, many duplicates, or requiring external sorting), the best choice of algorithm may vary. Always analyze the problem's constraints before selecting the most appropriate sorting algorithm.

