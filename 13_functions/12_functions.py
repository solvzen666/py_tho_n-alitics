# 12.
# Напишите функцию, которая возводит число в отрицательную степень число с помощью рекурсии.
# В качестве аргументов подаются целое положительное число n (число)
# и целое отрицательное число m (степень).

def power(a, n):
    if a == 0:
        return 0
    elif n == 0:
        return 1
    elif n == 1:
        return a
    elif n < 0:
        return 1 / (a * power(a, -n - 1))
    else:
        return a * power(a, n - 1)


a = float(input())
n = int(input())
print(power(a, n))