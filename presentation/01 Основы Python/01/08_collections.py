# Список (list): в квадратных скобках:
sleep_list = [
    'спать', 
    'дрыхнуть', 
    'кемарить',
    'спать'
] 

# Множество (set): в фигурных скобках, элементы выглядят как в списке,
# но не могут повторяться:
sleep_set = {
    'дрыхнуть', 
    'спать', 
    'кемарить'
} 
# Словарь (dict): в фигурных скобках, элементы выглядят как ключ:значение;
# ключи не могут повторяться:
sleep_dict = {
    'спать': 'дрыхнуть', 
    'почивать': 'кемарить'
}

# Есть ли элемент 'дрыхнуть' в списке sleep_list?
if 'дрыхнуть' in sleep_list:
    print('В списке: нашлось!') 
else:
    print('В списке: не нашлось :(')

# Есть ли элемент 'дрыхнуть' в сете sleep_set?
if 'дрыхнуть' in sleep_set:
    print('В сете: нашлось!') 
else:
    print('В сете: не нашлось :(')

# Есть ли элемент 'дрыхнуть' в словаре sleep_dict?
if 'дрыхнуть' in sleep_dict:
    print('В словаре: нашлось!') 
else:
    print('В словаре: не нашлось :(')







forest_list = ['лось', 'коза', 'барсук', 'глухарь', 'лиса', 'ёж']
               
if 'слонёнок' not in forest_list:
    print('но нету слонёнка в лесу у меня,')
    print('слонёнка весёлого нет!') 





# Задача 1
Добавьте в множество playlist несколько новых композиций (они собраны в списке new_music). Вызывать вручную метод add() для каждой новой записи будет нерационально, пусть за вас потрудится цикл for...in.
Плейлист станет больше и веселее!
playlist = {
    'Venus',
    'Yesterday',
    'Fireball',
    'Time',
    'Poison',
    'Thunderstruck'
}
new_music = [
    'Kashmir',
    'Smoke on the Water',
    'Bohemian Rhapsody',
    'Zombie',
    'Let It Be',
    'Its My Life',
]
for ...
    # Здесь ваш код

# Напечатайте множество






# РЕШЕНИЕ
playlist = {
    'Venus',
    'Yesterday',
    'Fireball',
    'Time',
    'Poison',
    'Thunderstruck'
}
new_music = [
    'Kashmir',
    'Smoke on the Water',
    'Bohemian Rhapsody',
    'Zombie',
    'Let It Be',
    'Its My Life',
]
for song in new_music:
    playlist.add(song)
    
print(playlist)







# ЗАДАНИЕ 2
"""Перед поездкой в командировку будет полезно покопаться в записной книжке и выяснить —
а кто из друзей живёт в том городе, куда предстоит поехать. Кто покажет город лучше, чем местный житель?
Для  этого напишите функцию is_anyone_in(collection, city). 
Для каждого неподходящего города функция должна напечатать фразу
В городе <название_города> у меня есть друг, но мне туда не надо.
Если кто-то из друзей живёт в запрошенном городе — функция должна напечатать фразу 
В городе <название_города> живёт <имя_друга>. Обязательно зайду в гости!"""

friends = {
    'Серёга': 'Омск', 
    'Соня': 'Москва', 
    'Дима': 'Челябинск', 
    'Алина': 'Хабаровск', 
    'Егор': 'Пермь'
}

def is_anyone_in(collection, city):
    for friend in ...
        if ...
            print(...)
        else:
            print(...)
    
is_anyone_in(friends, 'Хабаровск')







# РЕШЕНИЕ
friends = {
    'Серёга': 'Омск', 
    'Соня': 'Москва', 
    'Дима': 'Челябинск', 
    'Алина': 'Хабаровск', 
    'Егор': 'Пермь'
}

def is_anyone_in(collection, city):
    for friend in friends:
        if collection[friend] == city:
            print("В городе", collection[friend], "живёт", friend + ". Обязательно зайду в гости!")
        else:
            print("В городе", collection[friend], "у меня есть друг, но мне туда не надо.")

is_anyone_in(friends, 'Хабаровск')







# ЗАДАНИЕ 3
Ваша задача — разработать систему для работы сервисного центра всемирно известной компании "Cucumber". Она выпускает мобильные гаджеты и устройства для «умного дома».
Полный перечень техники производства "Cucumber" c указанием модельного ряда содержится в словарях mobile_devices и home_devices.
Каждый день компания присылает перечень устройств, поддержка которых прекращена. Перечень хранится в множестве not_supported_devices.
Задача программы — заполнить словарь result_catalog: в него должны попасть только те устройства, поддержку которых компания не прекратила. Ключами словаря должны быть названия устройств, а значениями — годы выпуска, например, 'cucuEar': 2018.

Выведите на экран строку 'Каталог поддерживаемых девайсов:'; на следующей строке напечатайте словарь result_catalog. 

Должно получиться примерно так:
    "Каталог поддерживаемых девайсов:"
    {'cucuLot': 2011, 'cucuMonitor': 2020, 'cucuEar': 2018, ...} 


mobile_devices = {
    'cucuPhone': 2010,
    'cucuBlet': 2013,
    'cucuClock': 2015,
    'cucuEar': 2018,
    'cuCube': 2015,
}

home_devices = {
    'cucuLot': 2011,
    'cucuBlock': 2010,
    'cucuWall': 2010,
    'cucuMonitor': 2020,
    'cucuLamp': 2015,
    'cucuTable': 2016,
    'cucuTV': 2017,
}

not_supported_devices = {'cucuBlock', 'cucuBlet', 'cucuWall'}
result_catalog = {}

# Допишите функцию выборки поддерживаемого девайса из словаря
def get_supported_catalog(dict_devices, device):
    supported_catalog = {}
    if device in dict_devices:
        ...
    return supported_catalog

all_devices = ...
supported_devices = ...

for device in ...:
    supported_mob_dev = get_supported_catalog(mobile_devices, device)
    # Добавьте значение в словарь result_catalog
    ...
    supported_home_dev = get_supported_catalog(home_devices, device)
    # Добавьте значение в словарь result_catalog
    ...

print('Каталог поддерживаемых девайсов: ')
print(result_catalog)




# РЕШЕНИЕ
mobile_devices = {
    'cucuPhone': 2010,
    'cucuBlet': 2013,
    'cucuClock': 2015,
    'cucuEar': 2018,
    'cuCube': 2015,
}

home_devices = {
    'cucuLot': 2011,
    'cucuBlock': 2010,
    'cucuWall': 2010,
    'cucuMonitor': 2020,
    'cucuLamp': 2015,
    'cucuTable': 2016,
    'cucuTV': 2017,
}

not_supported_devices = {'cucuBlock', 'cucuBlet', 'cucuWall'}

result_catalog = {}

# Допишите функцию выборки поддерживаемого девайса из словаря
def get_supported_catalog(dict_devices, device):
    supported_catalog = {}
    if device in dict_devices:
        supported_catalog[device] = dict_devices[device]
    return supported_catalog

all_devices = set(mobile_devices).union(set(home_devices))
supported_devices = set(all_devices).difference(set(not_supported_devices))

for device in supported_devices:
    supported_mob_dev = get_supported_catalog(mobile_devices, device)
                        # Добавьте значение в словарь result_catalog
    result_catalog.update(supported_mob_dev)
    
    supported_home_dev = get_supported_catalog(home_devices, device)
                         # Добавьте значение в словарь result_catalog
    result_catalog.update(supported_home_dev)

print('Каталог поддерживаемых девайсов: ')
print(result_catalog)
