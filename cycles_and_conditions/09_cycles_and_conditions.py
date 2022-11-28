#9
#Напишите программу, которая на вход получает число n и
# считает по нему сумму сумму 1! + 2! + 3! + ... + n!

# Ограничение: нельзя пользоваться готовой функцией factorial()
# из модуля math, функцией sum() и их аналогами.

# Формат ввода:
# 3
# Формат вывода:
# 9


n = int(input())
sum_of_factorials = 1
curr_factorial = 1
for i in range(2, n + 1):
    curr_factorial *= i
    sum_of_factorials += curr_factorial
print(sum_of_factorials)