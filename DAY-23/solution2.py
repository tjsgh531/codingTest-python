from collections import deque

def solution(prices):
    prices_arr = [(index, value) for index, value in enumerate(prices)]
    prices_queue = deque(prices_arr)

    answer = []
    for i in range(len(prices)):
        value = prices_queue.popleft();
        for value2 in prices_queue:
            if value[1] > value2[1] :
                answer.append(value2[0]-value[0])
                break
        else:
            answer.append(len(prices_arr)-value[0] - 1)

    return answer

print(solution([1,2,3,2,3]))