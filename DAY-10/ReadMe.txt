import datetime

datetime.datetime.strptime(data, format)
# datetime.datetime

날짜는 datetime클래스를 통해 나타내고, 날짜의 차이는 timedelta클래스를 통해 나타냅니다
=>나는 datetime객체를 계산하고싶다!!! 바꾸는 방법이 없을까?

=> datetime끼리 연산가능 but timedelta객체로 됨
        time1 = datetime(2018, 7, 13, 21, 40, 5)
        time2 = datetime.now()

        print(time2 - time1)    # 9 days, 23:18:54.6666
        print(type(time2 - time1))  #<class 'datetime.timedelta'>

=> timedelta로 시간 연산하기

        print((time2-time1).days, '일')
        print((time2-time1).seconds, '초')
        print((time2-time1).miliseconds, '백분의 일초')

=> 시간계산
        print(time2 + timedelta(days=5))
        print(time2 + timedelta(days=-3))
        print(time2 + timedelta(days=1,hours=-2))

    

