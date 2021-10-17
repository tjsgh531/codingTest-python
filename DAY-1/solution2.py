import re
def solution(new_id):

#step1
    answer = new_id.lower()

#step2
    answer = re.sub('[^a-z0-9\-_.]','',answer)

#step3
    answer = re.sub('\.+','[.]',answer)

#step4
    answer = re.sub('^[.]|[.]$','',answer)

#step5
#step6
    answer = 'a' if len(answer) == 0 else answer[:15]
    answer = re.sub('[.]$','',answer)
#step7
    if len(answer) <= 2 :
        while len(answer) == 3:
            answer = answer + answer[-1]

    return answer
