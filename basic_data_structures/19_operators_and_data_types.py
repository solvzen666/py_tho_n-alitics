# 19
# Напишите программу, которая запрашивает целое четырехзначное число и меняет
# местами его две первые и две последние цифры

n = int(input("Введите четырех значное число: "))
print(n % 100, n // 100, sep ='')

# % - остаток от деления, // - поделить без остатка