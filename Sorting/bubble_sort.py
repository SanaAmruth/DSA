

def swap (a, b):
    t = a
    a = b
    b = t
    return a,b
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i):
            if j+1<n and arr[j]>arr[j+1]:
                t = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = t
    return arr

if __name__== "__main__":
    arr = [4,9,34,1,3,2,1]
    print(f"Original array: {arr}")
    bubble_sort(arr)
    print(f"Final sorted array: {arr}")