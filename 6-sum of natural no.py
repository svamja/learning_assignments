square = 0
a = 0
b = 0
for i in range(1, 101):
    square += i ** 2
    a += i
a = a ** 2
b = a - square
print(b)
