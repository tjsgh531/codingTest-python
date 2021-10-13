이제 코드가 조금 멋있어지내 답보다 내가 더 멋있다고 느낄정도? ㅎ
1. zip사용(DAY-7)
    *병열처리 
    for a, b in zip(list1, list2):
        =>이런식으로 코드 짜면 리스트에서 값 하나씩 나옴

    *딕셔너리 또는 리스트 만들기
    dict(zip(list1,list2))
        => list1이 key값 list2가 value값으로 딕셔너리가 만들어짐
    
    list(zip(list1, list2))
        =>(list1[0],list2[0]) 형태의 원소를 갖는 리스트를 생성해줌

2. 내장형 for(DAY-7 level2)
    for을 한줄에 넣어서 사용하는 방식은 리스트 만들때만 가능