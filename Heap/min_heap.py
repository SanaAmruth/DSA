import sys
class Heap:
    def __init__(self, arr = []):
        self.arr = arr
        if arr is not None:
            self.build_heap()
    
    def parent(self, i):
        return (i-1) // 2

    def build_heap(self, ):
        n = len(self.arr)
        for i in range((n - 2) // 2, -1, -1):
            # print(i)
            self.heapify(i)
            # print(self.arr)
        # print(self.arr)

    def children(self, i):
        return 2 * i + 1, 2 * i + 2
    
    def value(self, i):
        if i >= len(self.arr):
            return sys.maxsize
        if i<0:
            return -sys.maxsize - 1
        return self.arr[i]

    def insert(self, val):
        self.arr.append(val)
        i = len(self.arr) - 1
        while self.parent(i) >= 0 and self.arr[i] < self.arr[self.parent(i)]:
            self.arr[i], self.arr[self.parent(i)] = self.arr[self.parent(i)], self.arr[i]
            i = self.parent(i)
        # print(self.arr)
    
    def heapify(self, idx):
        smallest = idx
        if self.value(2*idx+1)<self.value(smallest):
            smallest = 2*idx + 1
        if self.value(2*idx+2)<self.value(smallest):
            smallest = 2*idx + 2
        if smallest != idx:
            self.arr[smallest], self.arr[idx] = self.arr[idx], self.arr[smallest]
            self.heapify(smallest)

    def extract_min(self, ):
        min_value = self.arr[0]
        self.arr[0] = self.arr[len(self.arr)-1]
        self.arr.pop()
        self.heapify(0)
        return min_value
    
    def delete(self, idx):
        self.arr[idx] = -sys.maxsize - 1
        while self.value(self.parent(idx)) > self.value(idx):
            self.arr[idx], self.arr[self.parent(idx)] = self.arr[self.parent(idx)], self.arr[idx]
            idx = self.parent(idx)
        self.extract_min()

if __name__ == "__main__":
    heap1 = Heap()
    heap1.insert(4)
    heap1.insert(3)
    heap1.insert(2)
    heap1.insert(1)
    heap2 = Heap([4,3,2,1,9,8])
    heap1.delete(1)
    print(heap1.arr)
    print(heap1.arr)
    print(heap2.arr)