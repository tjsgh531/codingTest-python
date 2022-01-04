def solution(prices):
    prices_arr = [(index, value) for index, value in enumerate(prices)]

    answer = []
    for value in prices_arr:
        for value2 in prices_arr[value[0]:]:
            if value[1] > value2[1] :
                answer.append(value2[0]-value[0])
                break
        else:
            answer.append(len(prices_arr)-value[0] - 1)

    return answer

print(solution([1,2,3,2,3]))