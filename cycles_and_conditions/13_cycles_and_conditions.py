# 13
# Напишите программу, которая запрашивает у пользователя сторону
# квадрата и символ, а затем рисует этот символ по диагоналям квадрата.
# Гарантируется, что входное число всегда нечетное.


# Формат ввода:
# 5
# #

s = int(input('vv chislo: '))
char = str(input('vv simbol: '))
if s % 2 == 1:
    current_line = [' '] * s
    for i in range(0, s):
        current_line[i] = char
        current_line[s - 1 - i] = char
        print(''.join(current_line))
        current_line[i] = ' '
        current_line[s - 1 - i] = ' '