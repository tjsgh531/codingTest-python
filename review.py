import re
def solution(new_id):
#1
    id = new_id.lower()
#2
    id = re.sub("[^a-z0-9\-_.]",'',id)
#3
    id.replace('..','.')
    #id = re.sub["..",".",id]
#4
    if id.startswith('.'): id = id[1:]
    if id.endswith('.'): id = id[:-1]

    #if re.match('.',id) : id = id[1:]
    #if re.match('[a-z0-9\-_.]+.',id) : id = id[:-1]

#5
    if not(len(id)) :id ="a"
#6
    elif len(id) > 15 : id = id[:15] if id[14] != '.' else id = id[:14]
#7
    while len(id) < 3: id += id[-1]


    answer = id
    return answer