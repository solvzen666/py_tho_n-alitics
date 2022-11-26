# 16
# Часы показывают время в формате h:mm:ss (количество часов (от 0 до 23),
# двузначное количество минут, двузначное количество секунд).
# Количество минут и секунд при необходимости дополняются до
# двузначного числа нулями.
# Программа должна запрашивать количество секунд S,
# которое прошло с начала суток, и выводить в формате h:mm:ss,
# какое время будут показывать часы.

x = int(input())

hours = 0
minutes = 0
seconds = 0
days = 0

seconds += x % 60
minutes += (x // 60) % 60
hours += x // 60 // 60
days += x // 60 // 60 // 24
hours = hours - days * 24

days = str(days)
seconds = str(seconds)
minutes = str(minutes)
hours = str(hours)

if len(seconds) == 1:
    seconds = '0' + seconds

if len(minutes) == 1:
    minutes = '0' + minutes

if len(hours) == 1:
    hours = '0' + hours

print("day:", days)
print("time:", hours + ':' + minutes + ':' + seconds)

