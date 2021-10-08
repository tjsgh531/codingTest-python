ZIP함수

iterable 객체를 파라미터로 받음.

numbers = [1,2,3]
letters = ["A","B","C"]
for pair in zip(numbers, letters):
    print(pair)

#(1,"A")
#(2,"B")
#(3,"C")

병열처리
: 여러개 리스트를 한번씩 번갈아가며 실행 시키고 싶을 때
>>> for number, upper, lower in zip("12345", "ABCDE", "abcde"):
...     print(number, upper, lower)
...
1 A a
2 B b
3 C c
4 D d
5 E e

Unzip
:묶여 있는 것(튜플, 리스트도 가능 할까나?)을 두개 이상의 리스트로 나누고 싶을 때
>>> numbers = (1, 2, 3)
>>> letters = ("A", "B", "C")
>>> pairs = list(zip(numbers, letters))
>>> numbers, letters = zip(*pairs)

사전변환
: dictionary형으로 자료 변형
=> 이때, dict()함수 사용
>>> keys = [1, 2, 3]
>>> values = ["A", "B", "C"]
>>> dict(zip(keys, values))
{1: 'A', 2: 'B', 3: 'C'}