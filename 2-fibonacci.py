x = 0
y = 1
count = 0
total = 0
print("Fibonacci Number: ")
while count < 4000000:
    if count % 2 == 0:
        total += count
    x = y
    y = count
    count = (x + y)
    
    
print(count)
