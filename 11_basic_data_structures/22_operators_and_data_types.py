# 22
# Пусть организаторы мероприятия неправильно составили гугл-форму и
# просили людей указывать ФИО в неправильном порядке. Сначала спрашивали имя,
# потом отчество, затем фамилию. Напишите программу, которая будет
# переставлять ФИО в нужный порядок.

fio = input('Введите ФИО: ')
fio = ' '.join(fio.split()[2:] + fio.split()[:2])
print(fio)