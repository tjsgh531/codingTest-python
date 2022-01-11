import heapq
from collections import deque

def solution(jobs):
    time = 0
    currenttime = 0
    waitdisk =[]
    jobdisk = jobs[:]

    while(True):
        if len(jobdisk)== 0 and len(waitdisk)== 0 : break;

        appendwaitdisk, jobdisk = moveDisk(jobdisk, currenttime)
   
        for i in appendwaitdisk:
            item = (i[1], i[0])
            heapq.heappush(waitdisk, item)

        if(waitdisk):
            popitem = heapq.heappop(waitdisk)
            currenttime += popitem[0]
            taketime = currenttime - popitem[1]
            time += taketime
        else:
            latestdisk = jobdisk.popleft()
            currenttime = latestdisk[0];
    return time / len(jobs)

def moveDisk(jobdisk, time):
    disk = []
    jobdisk_queue = deque(jobdisk)
    print(f"time : {time}")
    print(f"jobdisk: {jobdisk}")
    for i in jobdisk:
        if i[0] <= time : 
            disk.append(i)
            jobdisk_queue.popleft()
        else:
            return disk, jobdisk_queue;
        
    return disk, jobdisk_queue;

print(solution([[0,3],[1,9],[2,6]]))
