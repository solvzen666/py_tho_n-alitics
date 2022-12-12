# Отличительная особенность методов объектов от простых функций состоит в том,
# что методу всегда передаётся ссылка на объект-экземпляр.
# Эта первый параметр метода и обычно он называется self.
# Название - не более чем соглашение: имя self не имеет абсолютно никакого
# специального смысла для языка Python. Но так принято

class Backpack:
    def add(self, item):
        print('В рюкзак положили ', item)
        self.content = item

my_backpack = Backpack()
my_backpack.add(item='ноутбук')

my_son_backpack = Backpack()
my_son_backpack.add(item='учебник')

print(Backpack.add)
print(my_backpack.add)

# аналогичны:
my_backpack.add(item="вода")
Backpack.add(self=my_son_backpack, item="вода")