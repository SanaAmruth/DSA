import sys

def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        temp = sys.maxsize
        for j in range(i, n):
            if arr[j]<temp:
                temp_idx = j
                temp = arr[j]
        arr[i], arr[temp_idx] = swap(arr[i], arr[temp_idx])

if __name__=="__main__":
    array = [4,9,34,1,3,2,1]
    print(f"Original array {array}")
    selection_sort(array)
    print(f"Sorted array {array}")