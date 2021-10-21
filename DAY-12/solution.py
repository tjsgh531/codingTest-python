class minHeap :
    def __init__(self, arr):
        if arr is not None:
            self.minheap = [None]+ arr
            self.minist(1)
        else:
            self.minheap = [None]
    
    def add(self,item):
        self.minheap.append(item)

        parent = len(self.minheap) // 2
        child = len(self.minheap) -1

        while parent > 1:
            if self.minheap[parent] > self.minheap[child]:
                self.minheap[parent], self.minheap[child] = self.minheap[child], self.minheap[parent]
                child = parent
                parent = child // 2
            else:
                break

    def pop(self):
        if len(self.minheap) > 1:
            self.minheap[1],self.minheap[-1] = self.minheap[-1],self.minheap[1]
            data = self.minheap.pop(-1)
            self.minist(1)
        else:
            data = None
        return data

    def minist(self, i): #i 아래로 맞춰주는 것
        left_child = i*2
        right_child = i*2 +1
        biggest = i

        if len(self.minheap) > left_child and self.minheap[left_child] < self.minheap[biggest]:
            biggest = left_child

        if len(self.minheap) > right_child and self.minheap[right_child] < self.minheap[biggest]:
            biggest = right_child

        if biggest != i:
            self.minheap[biggest],self.minheap[i] = self.minheap[i],self.minheap[biggest]
            self.minist(biggest)

def solution(scoville, K):
    scovillheap = minHeap(scoville)

    count = 0
    while True:
        minscv = scovillheap.pop()
        if minscv is None:
            return -1
        elif minscv >= K:
            return count
        else:
            minscv2 = scovillheap.pop()
            if minscv2 is None:
               return -1
            else:
                temp = minscv + minscv2*2
                scovillheap.add(temp)
                count += 1
                
