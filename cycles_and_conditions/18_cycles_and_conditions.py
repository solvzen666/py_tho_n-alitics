# 18
# Будем считать, что кубик может иметь неограниченное количество граней
# (натуральное число). Напишите программу, которая запрашивает,
# сколько граней имеется у двух разных кубиков. Затем выводит все возможные
# комбинации результатов бросков двух таких кубиков.

# Формат ввода:
# 2
# 3
# Формат вывода:
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3


a = int(input())
b = int(input())
if 0 < a <= 6:
    if 0 < b <=6:
        l1 = [s for s in range(1, a + 1)]
        l2 = [m for m in range(1, b + 1)]
        for i in range(len(l1)):
            for j in range(len(l2)):
                print(l1[i], l2[j])
    else: print("F")
else: print("F")