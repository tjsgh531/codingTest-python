def solution(p):
    if len(p) == 0:
        return ''

    count_open = 0
    count_close = 0
    for i in p:
        if i == '(': count_open += 1
        else : count_close += 1
        
        if count_close == count_open : break
    u = p[:count_open + count_close]
    v = p[count_open + count_close : ]
    
    if(isperfect(u)):
        return u + solution(v)
    else:
        return makePerfect(u,v)

def isperfect(str):
    
    if str[0] == ")":
        return False

    stack = []
    for value in str :
        if value == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
        else:
            stack.append(value)
    return True

def makePerfect(u,v):
    str_v = solution(v)
    answer = "(" + str_v + ")" #v 처리
    answer2 =[] #u 처리
    temp = u[1:-1]
    for i in temp:
        if i == "(":
            answer2.append(")")
        else :
            answer2.append("(")
        
    return answer + ''.join(answer2)

print(solution("()))((()"))