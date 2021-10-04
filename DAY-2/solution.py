def solution(lottos, win_nums):
    correct = 0
    var = 0
    for selectnum in lottos:
        for answernum in win_nums:
            if selectnum == 0: 
                var +=1
                break 
            elif selectnum==answernum: correct +=1

    min_rank = 7-correct if 7-correct < 7 else 6
    max_rank = 7-(correct + var)

    answer = [min_rank,max_rank]
    return answer