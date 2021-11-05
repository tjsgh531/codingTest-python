import collections

# list1 = ['aa', 'cc', 'dd', 'aa', 'bb', 'ee','bb', 'bb']
# print(collections.Counter(list1))

# print(collections.Counter({'가': 3, '나': 2, '다': 4}))

# c = collections.Counter(a =2, b =3, c=2)
# print(collections.Counter(c))

# c = collections.Counter(a=2, b=3, c=2)
# print(c)
# print(collections.Counter(c))
# print(sorted(c.elements()))

print(collections.Counter(A=3, B=2, C=10).elements())
print(list(collections.Counter(A=3, B=2, C=10).elements()))

print(collections.Counter("ABCDABBVDE").most_common()[0])