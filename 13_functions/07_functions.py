# 7.
# Почему не был создан новый список при повторном запуске функции?
# Объясните и исправьте.

def to_buy(*new_items, shopping_list = []):
    for i in new_items:
        shopping_list.append(i)
    return shopping_list

monday = to_buy('яблоки', 'молоко', 'хлеб')
print(monday)

tuesday = to_buy('груши', 'йогурт', 'мясо')
print(tuesday)
