import heapq 

def solution(operations):
    max_que = []
    min_que = []
    que_length = 0
    for i in operations:
        
        if i[0] == 'I':#큐에 추가
            if que_length == 0:
                max_que.clear()
                min_que.clear()
            que_length += 1
            num = int(i[2:])
            heapq.heappush(min_que, num)
            heapq.heappush(max_que, -num)

        elif i[:3] =='D -':# 큐 최솟값 삭제
            if que_length == 0: continue
            que_length -= 1
            heapq.heappop(min_que)

        else:# 큐 최대값 삭제
            if que_length == 0: continue
            que_length -= 1
            heapq.heappop(max_que)
    if que_length == 0: #큐가 비어있다
        return [0,0]
    else:
        return [-heapq.heappop(max_que),heapq.heappop(min_que)]

print(solution(["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]))