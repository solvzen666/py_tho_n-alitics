#23 У вас есть список с заказом в ресторане. Напишите программу, которая меняет
#   указанное по названию блюдо на другое. При этом новое блюдо в списке
#   будет расположено на месте того, что было заменено.

order = ['белое вино', 'салат Цезарь', 'паста Карбонара', 'чизкейк', 'шоколадный сорбет']
change_food = input()
input_food = input()
if change_food in order:
    index = order.index(change_food)
    order.remove(change_food)
    order.insert(index, input_food)
print(order)