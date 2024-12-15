a = 5
b = 3
c = 5

d = [1, 2, 3]
e = [1, 2, 3]
f = d

print(a == c)
print(a is c)

print(d == e)
print(d is e)

print(d == f)
print(d is f)

print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(id(e))
print(id(f))

a = 5
b = 5
c = a

print(id(a))
print(id(b))
print(id(c))
