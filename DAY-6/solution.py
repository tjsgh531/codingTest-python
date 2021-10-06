def solution(numbers):
    result = set(range(10))-set(numbers)
    answer = sum(list(result))
    return answer