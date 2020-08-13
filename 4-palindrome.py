def palindrome(num):
    return str(num) == str(num)[::-1]

# Bots are software programs that combine requests
# top Returns a reference to the top most element of the stack


def largest(bot, top):
    z = 0
    for i in range(top, bot, -1):
        for j in range(top, bot, -1):
            if palindrome(i * j):
                if i*j > z:
                    z = i*j
    return z


print(largest(100, 999))
