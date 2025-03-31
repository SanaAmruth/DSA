# Koko Eating Bananas - Solution Explanation

## Problem Statement
Koko loves to eat bananas and has `piles` of bananas. Each pile contains some number of bananas. There is a guard who comes back after `h` hours. Koko can eat at most `k` bananas per hour. Our goal is to find the **minimum** integer value of `k` such that Koko can eat all the bananas in `h` hours.

**Constraints:**
- Koko must eat bananas in a continuous manner (one pile at a time).
- She must finish a pile before moving to the next.
- She can take fractional time for a pile, but each hour she eats up to `k` bananas.

---

## Approach: Binary Search
Since the problem requires finding the **minimum** valid `k`, we can use **binary search** to efficiently find the optimal speed.

### **Steps to Solve:**
1. **Define the Search Space:**
   - The minimum possible speed is `1` (Koko eats at least 1 banana per hour).
   - The maximum possible speed is `10^9` (the largest banana pile, since Koko can finish one pile in an hour).

2. **Binary Search to Find the Minimum Speed `k`:**
   - We initialize `low = 1` and `high = 10^9`.
   - We check `mid = (low + high) // 2` as a potential eating speed.
   - Calculate `hours_taken(mid)`, which is the number of hours required if Koko eats `mid` bananas per hour.
   - If `hours_taken(mid) <= h`, update `k = mid` and **search for a smaller k** (`high = mid - 1`).
   - If `hours_taken(mid) > h`, increase the eating speed (`low = mid + 1`).
   - Continue until `low > high`.

3. **Calculate `hours_taken(piles, speed)`:**
   - This function computes the total hours required if Koko eats at a given speed.
   - We use `ceil(p / speed)` to determine the hours needed for each pile.
   - The formula `(p + speed - 1) // speed` efficiently computes the ceil without using floating-point operations.

---

## Code Implementation
```python
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_taken(piles, speed):
            # Calculate the total hours needed at a given speed
            return sum((p + speed - 1) // speed for p in piles)
        
        low, high = 1, 10**9
        k = high
        
        while low <= high:
            mid = low + (high - low) // 2
            h_needed = hours_taken(piles, mid)
            
            if h_needed <= h:
                k = mid  # Update the answer with the current valid speed
                high = mid - 1  # Try to find a smaller valid k
            else:
                low = mid + 1  # Increase speed since h_needed is too large
        
        return k
```

---

## **Time & Space Complexity**
- **Time Complexity:** `O(n log M)`, where:
  - `n` is the number of piles.
  - `M` is the maximum pile size (`10^9`), leading to `log(10^9) ≈ 30` iterations.
  - Each binary search iteration takes `O(n)`, making the total time complexity **O(n log M)**.
- **Space Complexity:** `O(1)`, since only a few extra variables are used.

---

## **Example Walkthrough**
### **Input:**
```python
piles = [3, 6, 7, 11]
h = 8
```

### **Binary Search Iterations:**
| `low` | `high` | `mid` | `hours_taken(mid)` | Action |
|-------|--------|--------|------------------|---------|
| 1     | 10^9   | 500000000 | Too small  | Decrease high |
| 1     | 500000000 | 250000000 | Too small  | Decrease high |
| ...   | ...    | ...   | ... | ... |
| 4     | 5      | 4      | 8  | Found valid k, try smaller |
| 3     | 3      | 3      | 10 | Too large, increase low |

Final **minimum eating speed `k`**: `4`

---

## **Key Takeaways**
✅ **Binary search** efficiently finds the minimum valid `k`.
✅ Using integer division `(p + speed - 1) // speed` avoids floating-point operations.
✅ Time complexity is `O(n log M)`, which is optimal for large inputs.
✅ This approach ensures that Koko eats all bananas within `h` hours while keeping `k` as low as possible.

