a=[1,2,3]
b=[1,2,3]
c=a
print(id(a))
print(id(b))
print(id(c))
print(a is not b)
print(c is a)
print(c is not b)