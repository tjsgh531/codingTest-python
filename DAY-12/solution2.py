import heapq

def solution(scoville, k):
    heap = heapq.heapify(scoville)
    count = 0
    while True:
        try:
            minvlaue = heapq.heappop(heap)
        except:
            return -1
        else:
            if minvlaue >= k: return count
            else:
                if len(heap) <= 2 : return -1
                else:
                    temp = minvlaue + heapq.heappop(heap)*2
                    heapq.heappush(temp)
                    
