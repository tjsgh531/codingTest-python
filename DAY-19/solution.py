import re
def solution(s):
    temp = re.sub('^[{]|[}]$',"",s)
    temp = re.sub('},',"}!",temp)
    targetlist = temp.split("!")
    targetlist.sort(key=len)
    
    answer =[]
    for value in targetlist:
        templist = re.findall('\d+',value)
        for item in templist:
            if item not in answer:
                answer.append(item)
    
    answer = list(map(int, answer))
    
    return answer;
    
#     temp = re.sub('},',"}!",temp)
#     targetlist = temp.split("!")
#     print(targetlist)

#     targetlist.sort(key=len)
#     print(targetlist)
    
#     answer =[]
#     for value in targetlist:
#         templist = re.findall('\d+',value)
#         print(templist)
#         for item in templist:
#             if item not in answer:
#                 answer.append(item)

#     answer = list(map(int, answer))
#     return answer;

solution("{{2,1,3,4},{2},{2,1},{2,1,3}}")
