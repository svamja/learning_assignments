import sympy
count = 2
num = []

while not len(num) == 10001:
    if sympy.isprime(count):
        num.append(count)
    count += 1
    
    
print(f"Prime Number: {num[10000]}")
