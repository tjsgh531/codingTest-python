import re
from itertools import product

def solution(N, number):
    
    if N == number:
        return 1;

    count = 2;
    exp = []
    mathtool = ['+','-','*','/']
    

    while count < 9:
        for i in range(count):
            exp.append('N');
            temp = [exp,mathtool]
            mathexp = list(product(*temp))
            

        count += 1

    answer = 0
    return answer

