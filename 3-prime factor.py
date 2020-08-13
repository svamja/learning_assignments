import math

# math.sqrt returns the square root of any number


def maxPrimeFactor(n):
   while (n % 2 == 0):
      max_Prime = 2

   for i in range(3, int(math.sqrt(n)) + 1, 2):
      while(n % i == 0):
         max_Prime = i
         n = n / i
   if n > 2:
      max_Prime = n
   return int(max_Prime)


n = 600851475143
print(maxPrimeFactor(n))
