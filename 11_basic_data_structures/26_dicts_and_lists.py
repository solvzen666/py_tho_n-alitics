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

# 26.
# Замените поход в театр на поход в кино в списке дел в пятницу вечером.

diary['пятница']['вечер'][0]='поход в кино'

days = ['понедельник', 'вторник', 'среда',
        'четверг', 'пятница','суббота', 'воскресенье']
for day in days:
    print(day, diary[day])