# 5
# Напишите программу, которая на вход получает число, а на выходе сообщает, простое это число или составное.

# Формат ввода:
# 169
# Формат вывода:
# Cоставное число

def isPrime(n):
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n
n = int(input())
prime = isPrime(n)
message = ("составное", "простое")[prime]
print(message)