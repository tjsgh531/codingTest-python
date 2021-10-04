import re
def solution(s):
    str = s
    result ={
        'zero' : '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9',
    }
    for i in result:
        str = re.sub(i,result[i],str)
    
    
    answer = int(str)
    return answer
