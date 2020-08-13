import time
import math

start = time.time()


def value(n):
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(math.sqrt(n) + 1)):
        index = i*2
        while index < n:
            is_prime[index] = False
            index = index + i

    prime = []
    for i in range(n):
        if is_prime[i] == True:
            prime.append(i)
    return prime


nth_prime = 100001
print(value(nth_prime))
