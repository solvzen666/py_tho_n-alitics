# 11.
# Напишите функцию, которая возводит число в положительную степень с помощью рекурсии.
# В качестве аргументов подаются целые положительные числа n (число) и m (степень).

def a(n, m):
    if (m == 1):
        return (n)
    if (m != 1):
        return (n * a(n, m - 1))
n = int(input("Введите число: "))
m = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", a(n, m))