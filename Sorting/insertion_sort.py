def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Test the implementation
if __name__ == "__main__":
    arr = [4,9,34,1,3,2,1]
    print(f"Original array: {arr}")
    insertion_sort(arr)
    print(f"Final sorted array: {arr}")