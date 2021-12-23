def solution(places):
    answer = []
    for classArr in places:
        if not checkRow(classArr):
            answer.append(0)
            continue
        if not checkCol(classArr): 
            answer.append(0)
            continue
        answer.append(1)
    return answer

# 가로행 확인
def checkRow(classArr):
    for r in range(0,5):
        tempStack =[None]
        for c in range(0,5):
            item = classArr[r][c]
            if tempStack[-1] == None : tempStack.append(item)
            
            elif tempStack[-1] == 'P':
                if item =='P': return 0
                elif item =='O':
                    if (r+1 < 5 and classArr[r+1][c] == 'P') or (r-1 >= 0 and classArr[r-1][c] == 'P') : return 0 #대각선 체크
                    tempStack.append('Q')
                else: tempStack.append(item)
            
            elif tempStack[-1] == 'Q':
                if item == 'P' : return 0
                else : tempStack.append(item)

            elif tempStack[-1] == 'O':
                if item == 'P':
                    if (r+1 < 5 and  classArr[r+1][c-1] == 'P') or (r-1 >=0 and classArr[r-1][c-1] == 'P') : return 0 #대각선 체크
                tempStack.append(item)
            else: tempStack.append(item)
    return 1

# 세로행 확인
def checkCol(classArr):
    for c in range(0,5):
        tempStack =[None]
        for r in range(0,5):
            item = classArr[r][c]
            if tempStack[-1] == None: tempStack.append(item)
            
            elif tempStack[-1] == 'P':
                if item == 'P': return 0
                elif item == 'O': 
                    if (c-1 >= 0 and classArr[r][c-1] == 'P') or (c+1 < 5 and classArr[r][c+1] == 'P'):#대각선 체크
                        return 0
                    tempStack.append('Q')
                else : tempStack.append(item)
            
            elif tempStack[-1] == 'Q':
                if item == 'P': return 0
                else : tempStack.append(item)
            
            else: tempStack.append(item)
    return 1
