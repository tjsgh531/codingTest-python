def solution(board, moves):
    
    boardset = board
    boardscale = len(board)
    picklist = []
    result = 0

    for row in moves :
        for i in range(boardscale):
            pick = boardset[i][row-1] 
            if pick == 0:
                continue
            else:
                picklist.append(pick)
                boardset[i][row-1] = 0
                break

    if len(picklist) != 0 :
        count = 0
        while True:
            if count > len(picklist)-2 : break
            if picklist[count] == picklist[count+1]:
                result +=2
                del picklist[count]
                del picklist[count]
                if count != 0 : count -=1
            else:
                count +=1



    answer = result
    return answer