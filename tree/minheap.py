import heapq

class MinHeap:
    def __init__(self):
        self.minheap = [None]

    def insert(self, item):
        self.minheap.append(item)
        
        current = len(self.minheap) -1

        while current > 1:
            parents = current // 2
            if self.minheap[current] < self.minheap[parents]:
                self.minheap[current], self.minheap[parents] = self.minheap[parents], self.minheap[current]
                current = parents
            else:
                break
    
    def pop(self):
        if len(self.minheap) > 1:
            self.minheap[1], self.minheap[-1] = self.minheap[-1],self.minheap[1]
            data = self.minheap.pop(-1)
            self.minHeapify(1)
        else:
            data = None
        return data

    def minHeapify(self, index):
        current = index
        left = current * 2
        right = current * 2 +1
        smallest = current

        if len(self.minheap) > left and self.minheap[left] < self.minheap[current]:
            smallest = left
        if len(self.minheap) > right and self.minheap[right] < self.minheap[current]:
            smallest = right
            
        if smallest != current:
            self.minheap[current], self.minheap[smallest] = self.minheap[smallest], self.minheap[current]
            self.minHeapify(smallest)
        else:
            pass

