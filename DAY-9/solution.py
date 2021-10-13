import math
def solution(progresses, speeds):
    timelist = [ math.ceil((100-value)/speed) for value,speed in zip(progresses, speeds) ] 
    
    maxvalue = (0, timelist[0])
    result = []
    for value, index in enumerate(timelist):
        if maxvalue[1] < value:
            result.append(index - maxvalue[0])
            maxvalue = (index,value) 

    result.append(len(timelist)- maxvalue[0])

    answer = result
    return answer