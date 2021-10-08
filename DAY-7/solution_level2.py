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

def solution2(record):
    nicknamedic = {rec.split(' ')[1] : rec.split(' ')[-1] for rec in record if not rec.split(' ')[0] != 'Leave'}
    printlist = [f"{nicknamedic[rec.split(' ')[1]]}님이 입장 했습니다." if rec.startswith('Enter') else f"{nicknamedic[rec.split(' ')[1]]}님이 퇴장하셨습니다." for rec in record if not rec.split(' ')[0] =='Change' ]