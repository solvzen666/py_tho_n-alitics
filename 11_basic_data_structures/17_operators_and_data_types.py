# 17
# Машина выезжает на нулевой километр МКАД и едет по часовой стрелке
# с постоянной скоростью V километров в час. На каком километре МКАД
# машина окажется через T часов? Длина МКАД: 109 км.

S = 109
T = int(input("Введите время в пути в минутах: "))
V = int(input("Введите постоянную скорость в пути: "))

print("Машина окажется на", V*T%S, "км МКАДа")