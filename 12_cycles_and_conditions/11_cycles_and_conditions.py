# 11

# Напишите программу, которая формирует список игроков женской команды
# по мини-футболу. Программа должна записывать возраст и пол претендента.
# Возраст должен запрашиваться после пола и только в том случае, если пол
# претендента женский. Если пол претендента мужской, программа должна
# сообщать о том, что он не подходит. Возраст претенденток должен быть
# от 18 до 35 лет. Если кандидат удовлетворяет требованиям, должно появляться
# соответствующее сообщение. Всего в команде могут быть только шесть человек.
# Когда необходимое число набирается, запись закрывается и выводится сообщение
# "Запись в команду закрыта".


x = 0
while x != 6:
    gender = input("Введите пол m/f: ")
    if gender == 'f':
        age = int(input("Введите возраст: "))
        if 18 <= age <= 34:
            print("Поздравляю! Вы в команде!")
            x += 1
        else:
            print('Извините, вы не подходите по возрасту')
    else:
        print('мальчики не нужны, приходите завтра')
if x == 6:
    print("В команде достаточное количество игроков, всем спасибо, все свободны!")