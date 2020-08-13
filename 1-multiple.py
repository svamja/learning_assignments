nums = [3, 5]
maximum = 1000


result = 0
for i in range(0, maximum):
    if i % 3 == 0 or i % 5 == 0:
        result += i
print(result)
