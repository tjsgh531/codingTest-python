def solution(numbers, hand):
    keypad = {
        1:(1,1),
        2:(1,2),
        3:(1,3),
        4:(2,1),
        5:(2,2),
        6:(2,3),
        7:(3,1),
        8:(3,2),
        9:(3,3),
        '*':(4,1),
        0:(4,2),
        '#':(4,3),
    }
    leftf = keypad['*']
    rightf = keypad['#']
    result = []
    
    for num in numbers:
        if num in [1,4,7]:
            result.append('L')
            leftf = keypad[num]
        elif num in [3,6,9]:
            result.append('R')
            rightf = keypad[num]
        else :
            numinkeypad = keypad[num]
            leftvalue = abs(leftf[0]-numinkeypad[0])+abs(leftf[1]-numinkeypad[1])
            rightvalue = abs(rightf[0]-numinkeypad[0])+abs(rightf[1]-numinkeypad[1])
            
            if leftvalue > rightvalue:
                result.append('R')
                rightf = keypad[num]
            elif leftvalue < rightvalue:
                result.append('L')
                leftf = keypad[num]
            else :
                if hand == 'right':
                    result.append('R')
                    rightf = keypad[num]
                else :
                    result.append('L')
                    leftf = keypad[num]
                    
    answer = ''.join(result)
    return answer