
def solution(new_id):
#step1
    client_id = new_id.lower()
    id_list = list(client_id)

    delete_list = []

#step2
    for i ,value in enumerate(id_list):
        if not(ord('0') <= ord(value) <=ord('9') or  ord('a') <= ord(value) <= ord('z') or value == '-'or value =='_' or value =='.'):
            delete_list.append(i)
            continue

    for i, index in enumerate(delete_list):
        del id_list[index - i]
    delete_list.clear()

#step3
    count = 0
    for i ,value in enumerate(id_list):
        if value == '.' :
            try:
                if id_list[i+1] == '.':
                    delete_list.append(i+1)
            except:
                break

    for i, index in enumerate(delete_list):
        del id_list[index - i]
    delete_list.clear()

#step4
    if id_list[0] == '.' :
        del id_list[0]
    if id_list[-1] == '.':
        del id_list[-1]

#step5
    if len(id_list) == 0:
        id_list.append('a')
#step6   
    while len(id_list) > 15:
        id_list.pop()

    if id_list[-1] == '.':
        del id_list[-1]

#step7
    temp = id_list[-1]
    while len(id_list) < 3:
        id_list.append(temp)

    answer = ''.join(id_list)
    return answer
