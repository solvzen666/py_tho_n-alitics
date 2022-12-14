diary = {'понедельник': {'утро': ['погулять с собакой'],
                         'день': [],
                         'вечер': ['погулять с собакой']},

         'вторник': {'утро': ['погулять с собакой'],
                     'день': [],
                     'вечер': ['погулять с собакой']},

         'среда': {'утро': ['погулять с собакой'],
                   'день': [],
                   'вечер': ['погулять с собакой']},

         'четверг': {'утро': ['погулять с собакой'],
                     'день': [],
                     'вечер': ['погулять с собакой']},

         'пятница': {'утро': ['заехать в шиномонтаж', 'помыть машину'],
                     'день': [],
                     'вечер': ['поход в театр', 'ужин в кафе']},

         'суббота': {'утро': [],
                     'день': [],
                     'вечер': []},

         'воскресенье': {'утро': [],
                         'день': [],
                         'вечер': []}}

#24
# Вам дан словарь c расписанием на неделю.
# Удалите ключи суббота и воскресенье. Вместо них добавьте пару, где ключ это кортеж суббота,
# воскресенье, а значение – список с делом посадить цветы на даче.


# Можно ли сделать ключ суббота, воскресенье списком?
# НЕТ
diary.pop('суббота')
diary.pop('воскресенье')
diary[('суббота', 'воскресенье')] = ['посадить цветы на даче']
days = ['понедельник', 'вторник', 'среда',
        'четверг', 'пятница', ('суббота', 'воскресенье')]
for day in days:
    print(day, diary[day])