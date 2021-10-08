def solution(w,h):
    sum = 0
    for i in range(w):
        sum += h*i // w

    answer = 2*sum
    return answer