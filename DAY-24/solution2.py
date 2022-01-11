import heapq
from collections import deque

def solution(jobs):
    jobs_disk = []
    for i in jobs:
        heapq.heappush(jobs_disk,i)

    wait_disk =[];
    
    currenttime = 0
    time = 0

    while(1):
        print(f"joobdisk : {jobs_disk}")
        print(f"waitdisk :{wait_disk}")
        if len(jobs_disk) > 0:
            if currenttime >= jobs_disk[0][0]: # 시작 할 수 있는 디스크가 있을 때 . waitdisk에 추가
                tempdisk = heapq.heappop(jobs_disk)
                tempdisk[0], tempdisk[1] = tempdisk[1], tempdisk[0]
                heapq.heappush(wait_disk,tempdisk)

            elif len(wait_disk) > 0: # 시작 할 수 있는 디스크가 job_disk에 없고 wait_disk가 있을때
                headdisk = heapq.heappop(wait_disk)
                time += currenttime + headdisk[0] - headdisk[1]
                currenttime += headdisk[0]
                print(f"currenttime : {currenttime}")
                print(f"time : {time}")

            else: #시작 할 것이 없는데 처리 할게 남았을 때
                tempdisk = heapq.heappop(jobs_disk)
                currenttime = tempdisk[0] + tempdisk[1]
                time += tempdisk[1];
        elif len(wait_disk) >0:
            headdisk = heapq.heappop(wait_disk)
            time += currenttime + headdisk[0] - headdisk[1]
            currenttime += headdisk[0]
            print(f"currenttime : {currenttime}")
            print(f"time : {time}")
        
        else : 
            break
            
    print(f"currenttime : {currenttime}")
    print(f"time : {time}")
    return time / len(jobs)
print(solution([[0,3],[1,9],[1,3],[1,3],[2,6],[100,3]]))