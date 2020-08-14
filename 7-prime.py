limit = 10001
x = 3
count = 1
prime = 2
while count < limit:
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            break
        else:
            prime = x
            count += 1
        i += 2

print(prime)
