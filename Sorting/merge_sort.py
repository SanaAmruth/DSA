def merge(array, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid
    L = array[low:mid+1]
    R = array[mid+1:high+1]

    merged_array = []
    i, j = 0, 0
    n1 = len(L)
    n2 = len(R)
    while i<n1 and j<n2:
        if L[i] <= R[j]:
            merged_array.append(L[i])
            i += 1
        else:
            merged_array.append(R[j])
            j += 1
    while i<n1:
        merged_array.append(L[i])
        i += 1
    while j<n2:
        merged_array.append(R[j])
        j += 1
    for i in range(low, high+1):
        array[i] = merged_array[i-low]

def mergeSort(array, low, high):
    if low < high:
        mid = low + (high - low) // 2
        mergeSort(array, low, mid)
        mergeSort(array, mid+1, high)
        merge(array, low, mid, high)


# Test the implementation
if __name__ == "__main__":
    arr = [4,9,34,1,3,2,1]
    print(f"Original array: {arr}")
    low = 0
    high = len(arr) - 1
    mergeSort(arr, low, high)
    print(f"Final sorted array: {arr}")

# Time complexity - O(nlogn)
# Space complexity - O(n)