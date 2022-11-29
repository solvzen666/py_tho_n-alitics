# 8.

def print_all(**kwargs):
    print(*kwargs.values(), sep=', ')


print_all(**{'1': 'яблоки', '2': 'молоко', '3': 'хлеб', '4': 'груши', '5': 'йогурт', '6': 'мясо'})
