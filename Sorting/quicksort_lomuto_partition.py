
def lomuto_partition(arr, low, high):
    ele = arr[high]
    p = low - 1
    for i in range(low, high):
        if arr[i]>ele:
            continue
        else:
            p += 1
            arr[i], arr[p] = arr[p], arr[i]
    p += 1
    arr[high], arr[p] = arr[p], arr[high]
    return p


def qsort(array, low, high):
    if low<high:
        p = lomuto_partition(array, low, high)
        qsort(array, low, p-1)
        qsort(array, p+1, high)


# Test the implementation
if __name__ == "__main__":
    arr = [4,9,34,1,3,2,1]
    print(f"Original array: {arr}")
    qsort(arr, 0, len(arr)-1)
    print(f"Final sorted array: {arr}")
