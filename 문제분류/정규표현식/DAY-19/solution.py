import re
def solution(s):
    temp = re.sub('^{|}$','',s)
    print(temp)

    test2 = re.findall('{[\d,]+}', s)
    print(test2)
    print(len(test2))

    return 0
    
    
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
