import sympy
n = int(input("Enter the value: "))
count = 2
num = []

while not len(num) == n:
    if sympy.isprime(count):
        num.append(count)
    count += 1
    
    
print(f"Prime Number: {num[n - 1]}")
