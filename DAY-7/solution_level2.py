def solution(record):

    recordlist = []
    nicknamedic = {}
    printlist = []

    for i in record:
        temp = i.split(' ')
        recordlist.append(temp)
    
    for rec in recordlist:
        state = rec[0]
        userid = rec[1]
        nickname = rec[2] if len(rec) > 2 else ''

        if userid not in nicknamedic:
            nicknamedic[userid] = nickname
        else:
            if nicknamedic.get(userid) != nickname and state != 'Leave':
                nicknamedic[userid] = nickname
        
            
    for rec in recordlist:
        state = rec[0]
        userid = rec[1]
        nickname = nicknamedic.get(userid)

        if state == 'Enter':
            printstr = "%s님이 들어왔습니다."%nickname
            printlist.append(printstr)    
            
        elif state == "Leave":
            printstr = "%s님이 나갔습니다."%nickname
        else:
            continue

    answer = printlist
    
    return answer

