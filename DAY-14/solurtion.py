import re
def solution(s):
    if len(s) == 0: return 1
    strlist =list(set(s))
    for value in strlist :
        if not(s == re.sub(value+'{2}','',s)):
            return solution(re.sub(value+'{2}','',s))
        else:
            continue
    return 0


    


print(solution("baabaa"))