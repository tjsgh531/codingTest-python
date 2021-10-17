def solution(scoville, K):
    scvlist = sorted(scoville)
    count = 0

    while scvlist[0] <= K:
        if len(scvlist) < 2:
            return -1;
        
        newitem = scvlist[0] + scvlist[1] * 2
        scvlist = scvlist[2:]
        scvlist.insert(0,newitem)
        
        count += 1
        scvlist = sorted(scvlist)  
    
    return count