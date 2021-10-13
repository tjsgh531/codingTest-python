import datetime
import re
import time

def solution(lines):
    lineslist = [line.split() for line in lines]
    callineslist = []
    for value in lineslist:
        end = time.mktime(datetime.datetime.strptime(value[0]+value[1],"%Y-%m-%d%H:%M:%S.%f").timetuple())
        taketime = float(re.sub('s$','', value[-1]))
        start = end - float(datetime.timedelta(seconds=taketime).total_seconds()) + float(datetime.timedelta(seconds=0.001).total_seconds())
        callineslist.append((start, end))

    for value in callineslist:
        print (datetime.datetime.fromtimestamp(value[-1]))


    maxonprocessnum = 0

    for value in callineslist:
        
        starttime = value[0]
        count = 0
        for val in callineslist:
            if starttime <= val[0] <= starttime + 1.0: count += 1 
            elif starttime < val[0] : break
        if maxonprocessnum < count : maxonprocessnum = count

    return maxonprocessnum