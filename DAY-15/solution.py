import copy
def solution(rows, columns, queries):
    
    bord = [ [(r-1) * columns + c for c in range(1,columns+1)] for r in range(1, rows+1)]
    answer = []

    for y1, x1, y2, x2 in queries:
        minimum = None
        temp = copy.deepcopy(bord)
        
        for i in range(x1, x2):
            if minimum is None or minimum > bord[y1-1][i]: minimum = bord[y1-1][i]
            bord[y1-1][i] = temp[y1-1][i-1]


        for i in range(y1,y2):
            minimum = min(minimum,bord[i][x2-1])
            bord[i][x2-1] = temp[i-1][x2-1] 

   
        for i in range(x1-1, x2-1):
            minimum = min(minimum,bord[y2-1][i])
            bord[y2-1][i] = temp[y2-1][i+1] 

        
        for i in range(y1-1,y2-1):
            minimum = min(minimum, bord[i][x1-1])
            bord[i][x1-1] = temp[i+1][x1-1]

        
        answer.append(minimum)
        print(minimum)

    return answer

solution(3,3,[[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]])