#   Задача 6

# Питон выполз на улицу погулять и решил поиграть: просил прохожих назвать какую-нибудь цифру
# (т.е. ввести её с клавиатуры) и приписывал эту цифру к цифре, которую назвал предыдущий
# прохожий. Написать код, который позволит определить, какое число получится после опроса
# четырёх прохожих, если известно, что первый прохожий назвал цифру 5. Задача не подразумевает
# использование циклов; запускать код несколько раз / копировать строки кода или ячейки можно.
# Внимание: в результате должно получиться целое число, не строка.

input_random_score_0 = str(5)
input_random_score_1 = input("Вводите числа через Enter")
input_random_score_2 = input()
input_random_score_3 = input()
input_random_score_4 = input()

if input_random_score_1.isdigit():
    if input_random_score_2.isdigit():
        if input_random_score_3.isdigit():
            if input_random_score_4.isdigit():
                s = int(input_random_score_0 + input_random_score_1 +
                    input_random_score_2 + input_random_score_3 + input_random_score_4)
                print("Получившееся число = ", s)
            else: print("Неудача")
        else: print("Неудача")
    else: print("Неудача")
else: print("Неудача")