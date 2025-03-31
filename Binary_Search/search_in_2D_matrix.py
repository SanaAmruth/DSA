# https://neetcode.io/problems/search-2d-matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Helper function to perform binary search on a given list (row)
        def binary_search(arr, low, high, target):
            while low <= high:
                mid = low + (high - low) // 2  # Calculate the middle index
                if arr[mid] == target:  # If the target is found at the middle
                    return True
                elif arr[mid] < target:  # If the target is greater than the mid element, search the right half
                    low = mid + 1
                else:  # If the target is smaller than the mid element, search the left half
                    high = mid - 1
            return False  # Return False if the target is not found in the current row

        # Helper function to find the potential row using binary search on the first column of each row
        def get_row(arr, target):
            n = len(arr)  # Length of the array (number of rows in the matrix)
            idx = [n, False]  # Initialize the index as [n, False] (n is a placeholder)
            low, high = 0, n - 1  # Set initial low and high pointers for binary search
            while low <= high:
                mid = low + (high - low) // 2  # Calculate the middle index
                if arr[mid] == target:  # If the target matches the first element of the row
                    return [mid, True]  # Return the row index and a flag indicating that the target was found
                elif arr[mid] > target:  # If the target is smaller, search in the left half of the rows
                    idx = [mid, False]  # Set the index to the current row as a potential match
                    high = mid - 1  # Move the high pointer to the left half
                else:  # If the target is larger, search in the right half of the rows
                    low = mid + 1  # Move the low pointer to the right half
            return idx  # Return the index as [low, False] if no exact match is found

        # Call get_row to determine the potential row in which the target might be found
        idx = get_row([row[0] for row in matrix], target)

        # If the exact match was found in the first column, return True
        if idx[1] == True:
            return True
        
        # If not found, we need to check the row just before the identified row
        row = matrix[idx[0] - 1]

        # Perform binary search on the row to find the target
        return binary_search(row, 0, len(row) - 1, target)

# Time complexity - O(logm + logn) --> O(log(m*n))