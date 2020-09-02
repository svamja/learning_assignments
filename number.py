n = int(input("Enter the number: "))

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Is is not a Prime number.")
            break
    else:
        print("It is a Prime number.")
