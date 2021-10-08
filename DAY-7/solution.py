def solution(absolutes, signs):
    result = []
    for i, value in enumerate(signs):
        if value == '-':
            result.append(-absolutes[i])
        else:
            result.append(absolutes[i])
    
    answer = sum(result)
    return answer