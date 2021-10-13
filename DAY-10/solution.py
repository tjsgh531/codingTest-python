import datetime
import enum
import re

def solution(lines):
    lineslist = [line.split() for line in lines]
    callineslist = []
    for value in lineslist:
        end = datetime.datetime.strptime(value[0]+value[1],"%Y-%m-%d%H:%M:%S.%f")

        taketime = float(re.sub('s$','', value[-1]))
        start = end - datetime.timedelta(seconds=taketime) + datetime.timedelta(seconds=0.001)
        callineslist.append((start, end))

    time = callineslist[0][0] 
    lasttime = callineslist[-1][-1]

    maxonprocess = 1
    for index,value in enumerate(callineslist) :
        if index == 0 : continue
        for check in range(index-1) :
            if value[0] < callineslist(check)[-1]:
                if index+1
    
    return maxonprocess