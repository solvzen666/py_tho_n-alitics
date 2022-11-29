# 13.
# Напишите функцию, которая находит число Фиббоначи по его номеру.
# В качестве аргумента подается целое положительное число n (число).

def fibonachchi(n):
    if n < 2:
        return 0
    x = y = 1
    for i in range(2, n-1):
        y, x = y + x, y
    return y
print(fibonachchi(77))