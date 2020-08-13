def is_divisible(n):
    for divisor in range(2, 21):
        if n % divisor != 0:
            return False
        return True


number = 1
while not is_divisible(number):
    number += 1
print(number)
