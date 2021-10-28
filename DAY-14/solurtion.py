def solution(s):
    stack = [None]
    for value in s:
        if stack[-1] == value:
            stack.pop()
        else:
            stack.append(value)
    return 1 if len(stack) == 1 else 0


    


print(solution("baabaa"))