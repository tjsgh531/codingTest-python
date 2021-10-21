class MaxHeap:
    def __init__(self):
        self.maxheap = [None]

    def insert(self,item): # maxHeapify에 의존 x => maxHeapify는 heap의 처음을 다루는 아이/ 얘는 끝에 더해서 알아서 정렬 해줘야해 ㅜㅜ
        self.maxheap.append(item)
        current = len(self.maxheap) -1
        parents = current //2

        while current > 1:
            if self.maxheap[current] > self.maxheap[parents]:
                self.maxheap[current], self.maxheap[parents] = self.maxheap[parents], self.maxheap[current]
                current = parents
                parents = current // 2
            else:
                break

    def pop(self):
        if len(self.maxheap) > 1:
            self.maxheap[1], self.maxheap[-1] = self.maxheap[-1], self.maxheap[1]
            data = self.maxheap.pop(-1)
        else:
            data = None
        return data

    def maxHeapify(self, index): #root가 사라졌을 때
        current = index
        left = current * 2
        right = current * 2 + 1
        biggest  = current

        if len(self.maxheap) > left and self.maxheap[current] < self.maxheap[left]:
            biggest = left

        if len(self.maxheap) > right and self.maxheap[current] < self.maxheap[right]:
            biggest = right

        if biggest != current:
            self.maxheap[biggest], self.maxheap[current] = self.maxheap[current], self.maxheap[biggest]
            self.maxHeapify(biggest)
        else:
            pass
