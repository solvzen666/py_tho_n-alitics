# В Python свойства называются атрибутами, а действия - методами
# Ссылки на атрибуты и методы используют синтаксис,
# использующийся для всех ссылок на атрибуты
# в Python: объект, имя.
# Простейшая форма определения класса
# class ClassName:
#     < выражение - 1 >
#     .
#     .
#     .
#     < выражение - N >

class Toyota:
    def __init__(self):
        self.current_velocity = "0 км/ч"
        self.color = "Black"
        self.price = "1 000 000 руб"
        self.max_velocity = "200 км/ч"
        self.engine_rpm = 0

    def start(self):
        self.engine_rpm = 5000

    def go(self):
        self.current_velocity = "20 км/ч"

# Класс - это как лекало для производства объектов.
produced, plan = 0, 10000
stock = []
while produced < plan:
    new_car = Toyota()
    stock.append(new_car)
    produced += 1
# мы можем произвести сколько угодно объектов

# Одинаковые объекты описываются одним классом
my_car = Toyota()

print(my_car.color)
print(my_car.price)
print(my_car.max_velocity)
print(my_car.engine_rpm)
print(my_car.current_velocity)

# Объекты имеют действия,
# которые с ними можно производить.
# Некоторые свойства объектов могут менятся
# после действий над объектами.
my_car.start()
print(my_car.engine_rpm)

my_car.go()
print(my_car.engine_rpm)
print(my_car.current_velocity)



class Robot:
    def __init__(self):
        self.name = "R2D2"

    def hello(self):
        print("Привет, Мир! Я - ", self.name)

# создаем новый объект (экземпляра класса)
# и присваиваем локальной переменной robot ссылку на него
robot = Robot()
robot.hello()

# переменные только ссылаются на объект
some_var = robot
some_var.hello()

some_robot = some_var
some_robot.hello()

some_robot.name = "C-3PO"
some_robot.hello()

robot.hello