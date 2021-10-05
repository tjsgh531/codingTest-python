def solution(s):
    str = s
    if len(str) > 1 :
        result = 1000
        for i in range(1, (len(str)//2)+1):
            splitleght = i
            splitstr = []

            start = 0
            end = 0
            while True:
                start = end
                end += splitleght
                if end <= len(str):
                    splitstr.append(str[start:end])
                elif start < len(str) :
                    splitstr.append(str[start:])
                else:
                    break

            count = 1 
            for i in range(len(splitstr)):

                if i != len(splitstr)-1 and splitstr[i] == splitstr[i+1]:
                    splitstr[i] = ''
                    count +=1
                else:
                    if count != 1:
                        splitstr[i] = "%d%s"%(count,splitstr[i])
                        count = 1

            if result > len(''.join(splitstr)):        
                result = len(''.join(splitstr))         


    else :
        result = 1
    answer = result
    return answer