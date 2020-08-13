count = 2
total = 0
while count < 4000000:
    if count % 2 == 0:
        total += count
    count += (count - 1)
print(count)
