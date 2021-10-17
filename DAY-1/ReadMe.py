# 대소문자 바꾸기
# upper() / lower() / swapcase() / capitalize()/ title() 
print("대소문자 바꾸기")
str = "abcDEfgH"
print(str.upper())
print(str.lower())
print(str.swapcase())

# 값 있는지 없는지
# find() / rfind() / index() / in / not in 
print("\n값 있는지 없는지")
str = "abcdeafgh"
print(str.find('a'))
print(str.rfind('a'))
print(str.index('a'))
print('a' in str)
print('h' not in str)

# 바꾸기(모두 바뀜)
# replace() 
print("\n바꾸기(모두 바뀜)")
str = "ab2cd2fg2dd"
str = str.replace('2', '*')
print(str)

# 시작 끝 확인
# startswith() / endswith() 

# 나누기 합치기
# join(list) / split() / rsplit() / partition() / rpartition()
print("\n나누기 합치기")
str = "!a@b#c$d"
listA = ['l','e','e','s','u','n','h','o']
print(''.join(listA))
print(''.split(str))
print(*str)
print(''.partition(str))
strlist =  list(str)
print(strlist)

# count() 해당 원소 개수 
# strip() / rstrip() / lstrip()
