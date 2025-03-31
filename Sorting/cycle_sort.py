

def cycle_sort(arr):
    n = len(arr)
    # i = 0
    for i in range(n-1):
        key = arr[i]
        temp = 0
        for j in range(i+1,n):
            if arr[j]<key:
                temp += 1
        arr[i], arr[i+temp] = arr[i+temp], arr[i]
        while(temp!=0):
            key = arr[i]
            temp = 0
            for j in range(i+1,n):
                if arr[j]<key:
                    temp += 1
            arr[i], arr[i+temp] = arr[i+temp], arr[i]
    return arr

# Test the implementation
if __name__ == "__main__":
    arr = [4,9,34,1,3,2]
    print(f"Original array: {arr}")
    cycle_sort(arr)
    print(f"Final sorted array: {arr}")