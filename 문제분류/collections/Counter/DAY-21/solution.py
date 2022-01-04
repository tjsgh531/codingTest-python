from collections import Counter

def solution(str1, str2):
    upperstr1 = str1.upper();
    upperstr2 = str2.upper();

    str1Arr = []
    temp1 = [];
    for value in upperstr1:
        if value.isalpha():
            temp1.append(value)
            if len(temp1) < 2:
                continue
            else:
                str1Arr.append(''.join(temp1[-2:]))
        else:
            temp1.clear()

    str2Arr = []
    temp2 = [];
    for value in upperstr2:
        if value.isalpha():
            temp2.append(value)
            if len(temp2) < 2:
                continue
            else:
                str2Arr.append(''.join(temp2[-2:]))
        else:
            temp2.clear()

    str1dic = Counter(str1Arr)
    str2dic = Counter(str2Arr)

    commonele = list(set(str1Arr) & set(str2Arr))
    diffele = list((set(str1Arr) | set(str2Arr)) - set(commonele))

    common_num = 0
    for value in commonele:
        common_num += min(str1dic[value], str2dic[value])

    print(f"commonNum : {common_num}")

    diff_num = 0
    for value in commonele:
        diff_num += max(str1dic[value], str2dic[value])
    for value in diffele:
        diff_num += max(str1dic[value], str2dic[value])

    print(f"diffNum : {diff_num}")

    if diff_num == 0 & common_num == 0:
        return 65536
    
    result = (float(common_num) / float(diff_num))*65536.0
    print(result)
    answer = int(result)
    return answer

print(solution("aaa", "aaaa"));