# 15
# Рабочие клеили обои на стены. Первую стену поклеили за M минут, а каждую следующую
# на 5 минут больше, чем предыдущую. Напишите программу, которая запрашивает сколько стен
# было в квартире под поклейку, а также время работы с первой стеной в минутах.
# Программа должна выводить, сколько часов рабочие потратили на поклейку обоев во всей квартире.
# Час отсчитывается с первой минуты. Ответом должно быть целое число.

# Формат ввода:
# 6
# 10
# Формат вывода:
# 3

import math
m = int(input("количество стен: "))
n = int(input("время работы с первой стеной: "))
s = 0
for i in range(m):
    n += 5
    s += n
print(math.ceil(s/60))