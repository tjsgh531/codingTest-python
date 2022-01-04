test1 = "is Alpha"
test2 = "isAlpha"
test3 = "이즈Alpha"
test4 = "is1Alpha"

def isAlpha(string):
    return string.isalpha()

# print(isAlpha(test1))
# print(isAlpha(test2))
# print(isAlpha(test3))
# print(isAlpha(test4))

test1 = "12345"
test2 = "12 345"
test3 = "12ab45"
test4 = "123가나"

def isDigit(string) :
    return string.isdigit()

# print(isDigit(test1))
# print(isDigit(test2))
# print(isDigit(test3))
# print(isDigit(test4))

test1 ="12가나ab"
test2 = "12 가나ab"
test3 ="가나다라ab"
test4 ="abcd"
test5 = "1234"

def isAlnum(string):
    return string.isalnum()

print(isAlnum(test1))
print(isAlnum(test2))
print(isAlnum(test3))
print(isAlnum(test4))
print(isAlnum(test5))