# Задача 3

# Тест по английскому языку состоит из трёх частей. Ученик
# последовательно вводит с клавиатуры набранные баллы за каждую
# часть – три целых числа. Каждое число вводится на отдельной строке,
# то есть input() запрашивается три раза. Написать программу, которая
# считает итоговый балл за тест – сумму баллов за три части.

input_test_score_0 = input("Введите последовательно ваши оценки за тест: ")
input_test_score_1 = input()
input_test_score_2 = input()
if input_test_score_0.isdigit():
    if input_test_score_1.isdigit():
        if input_test_score_2.isdigit():
            S = int(input_test_score_0) + int(input_test_score_1) + int(input_test_score_2)
            print("Ваш общий балл за тест = ", S)
        else:
            print("введено некорректное значение за номером 3")
    else:
        print("введено некорректное значение за номером 2")
else:
    print("введено некорректное значение за номером 1")