import re
import itertools
def solution(expression):
    answer = 0
    numlist = re.findall('\d+', expression)
    operatorlist = re.findall('\D',expression)
    operatorlist.append(None) #zip사용할려고 개수 맞쳐줌 + 끝인거 알기 위해
    expressionlist = []
    for num, oper in zip(numlist, operatorlist):
        expressionlist.append(num)
        expressionlist.append(oper)

    operatorlist.pop()
    expressionlist.pop()
    orderlist = itertools.permutations(list(set(operatorlist)))

    for orderele in orderlist:
        calculatedlist = expressionlist[:]
        for oper in orderele:
            calculatedlist = calculator(calculatedlist, oper)
        answer = max(answer, abs(int(calculatedlist[0])))

    return answer    
    
def calculator(exp, oper):
    stack = []
    temp = []
    for value in exp:
        if len(temp) > 0:
            temp.append(value)
 
            stack.append(str(eval(''.join(temp))))
            temp.clear()
            continue

        if value == oper :
            temp.append(stack.pop())
            temp.append(value)
        else:
            stack.append(value)
    return stack