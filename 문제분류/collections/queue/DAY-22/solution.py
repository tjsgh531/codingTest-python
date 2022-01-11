from collections import deque

def solution(priorities, location):
    order = sorted(priorities)
    temp = [ (index, value) for index, value in enumerate(priorities)]
    
    q = deque(temp)

    return findanswer(q, location, order)
    
def findanswer(q, location, order):
    answer = 1

    maxnum = order.pop()
    while(1):
        value = q.popleft()
        print(answer)
        if value[1] == maxnum :
            print(value, location)
            if value[0] == location:
                return answer
            else:
                answer += 1
                maxnum =order.pop()
                continue
        else:
            q.append(value)
 

print(solution([2, 1, 3, 2], 0))