concert_songs = {
    'Ничего на свете лучше нету',
    'Мы к вам заехали на час',
    'Рок-колыбельная',
    'Луч Солнца Золотого',
    'Ничего на свете лучше нету',
    'Куда ты, тропинка, меня завела',
    'А как известно, мы народ горячий'
}
# Выясним, к какому типу данных принадлежит переменная concert_songs
# для этого есть встроенная в Python функция type()
print(type(concert_songs))

# Напечатаем содержимое переменной concert_songs
print(concert_songs)
# Команда print(type(concert_songs)) вывела в терминал строку <class 'set'>.
# Проверка подтверждает: тип переменной concert_songs — set. 






# Объявляем список bremen_musicians 
bremen_musicians = ['Трубадур', 'Кот', 'Пёс', 'Осёл', 'Петух']

# Обращаемся к элементу по индексу
print(bremen_musicians[1])
# Будет напечатано: Кот

# Объявим множество songs (фигурные скобки!)
songs = {
    'Ничего на свете лучше нету',
    'Мы к вам заехали на час',
    'Рок-колыбельная'
}

# Обращаемся к элементу по индексу
print(songs[2])
# "Ошибка: set не поддерживает индексы"





# Напечатаем афишу. Названия песен будут напечатаны в случайном порядке, ведь unique_songs — это множество.
# Но такая непредсказуемость внесёт некоторую интригу в программу концерта. 
unique_songs = {
    'Рок-колыбельная',
    'Ничего на свете лучше нету',
    'Мы к вам заехали на час',
    'А как известно, мы народ горячий',
    'Луч Солнца Золотого',
    'Куда ты, тропинка, меня завела'
}
# Сначала напечатаем заголовок афиши
print('Только один концерт! Проездом из Бремена в Рио-де-Жанейро!')
print('БРЕМЕНСКИЕ МУЗЫКАНТЫ!')

# Объявляем цикл
for song in unique_songs:
    print(song)

# А эта строка выполнится после того,
# как цикл закончит работу
print('Не опаздывайте, начало в 19:00')







# Применим метод add() к объекту playlist.
# Аргументом будет строка 'Thunderstruck'; метод add() добавит новый элемент в множество playlist.
playlist = {
    'Venus',
    'Yesterday',
    'Fireball',
    'Time',
    'Poison'
}

playlist.add('Thunderstruck')
print(playlist)
# Будет напечатано, например: 
# {'Yesterday', 'Fireball', 'Thunderstruck', 'Poison', 'Venus', 'Time'}
# Элементы множеств никогда не соблюдают порядок! 






# Объединение двух множеств

# В результате будет создано новое, третье множество (а оба исходных останутся такими, как были).
playlist_1 = {'Три белых коня', 'Happy new year', 'Снежинка'}
playlist_2 = {'Last christmas', 'Снежинка', 'Happy new year'}
playlist_3 = playlist_1.union(playlist_2)

print(playlist_3)




# Поиск различий в двух множествах

# Метод set_1.difference(set_2) вернёт новое множество,
# оно будет содержать только те элементы, которые присутствуют в set_1, но отcутствуют в set_2;
# это похоже на «вычитание»: set_1 - set_2.
# Ни одно из исходных множеств не изменится.
playlist_1 = {'Голубой вагон', 'Облака', 'Yesterday', 'Наше лето'}
playlist_2 = {'Наше лето', 'Голубой вагон', 'Облака'}
playlist_3 = playlist_1.difference(playlist_2)

print(playlist_3)







# ЗАДАНИЕ 1
Напишите функцию add_cities(), которая добавит элементы из списка new_cities в all_cities. 
Метод union() для этой задачи не подходит, ведь вам нужно добавить элементы в существующее множество, а не создать новое.
def print_valid_cities(all_cities, used_cities):
    diff = all_cities.difference(used_cities)
    for city in diff:
        print(city)

def add_cities(all_cities, new_cities):
    # Напишите код функции
 
# эти города нужно добавить в множество all_cities 
new_cities = [
    'Екатеринбург',
    'Выборг' ,
    'Владивосток',
    'Казань',
    'Why',
    'Йезд'
]

all_cities = {
    'Абакан',
    'Астрахань', 
    'Бобруйск', 
    'Калуга',
    'Караганда',
    'Кострома',
    'Липецк', 
    'Новосибирск'
}

used_cities = {
    'Калуга',
    'Абакан' ,
    'Новосибирск'
}

add_cities(all_cities, new_cities)
print_valid_cities(all_cities, used_cities)



# РЕШЕНИЕ
def print_valid_cities(all_cities, used_cities):
    diff = all_cities.difference(used_cities)
    for city in diff:
        print(city)


def add_cities(all_cities, new_cities):
    for city in new_cities:
        all_cities.add(city)

new_cities = [
    'Екатеринбург',
    'Выборг' ,
    'Владивосток',
    'Казань',
    'Why',
    'Йезд'
]

all_cities = {
    'Абакан',
    'Астрахань', 
    'Бобруйск', 
    'Калуга',
    'Караганда',
    'Кострома',
    'Липецк', 
    'Новосибирск'
}

used_cities = {
    'Калуга',
    'Абакан' ,
    'Новосибирск'
}

add_cities(all_cities, new_cities)
print_valid_cities(all_cities, used_cities)






# ЗАДАНИЕ 2
Вам нужно написать программу, которая найдёт одинаковые элементы в двух списках.

Допишите функцию get_together_games(): она должна принимать на вход два списка, а возвращать — множество игр, названия которых есть в обоих списках.
Получите из функции это множество и построчно напечатайте его элементы (названия игр); перед названием каждой игры поставьте эмоджи 👾 и пробел. Эмоджи — это текстовый символ, как дефис или буква, его можно скопировать из условия и вставить в код.
Результат должен выглядеть примерно так:
👾 Super Hero Developer
👾 Python Shooter
👾 Online-backgammon 


def get_together_games(...):
    # Напишите здесь код функции для поиска пересечений

anfisa_games = [
    'Online-chess',
    'Города',
    'DOOM',
    'Крестики-нолики'
]
alisa_games = [
    'DOOM',
    'Online-chess',
    'Города',
    'GTA',
    'World of tanks'
]
# Вызовите функцию со списками игр в качестве параметров
together_games = ...
# Напечатайте итоговый перечень игр в цикле
for ... in ...:
    print(...)





# РЕШЕНИЕ
def get_together_games(games_1, games_2):
    together_games = set(games_1).intersection(set(games_2))
    return together_games
    

anfisa_games = [
    'Online-chess',
    'Города',
    'DOOM',
    'Крестики-нолики'
]
alisa_games = [
    'DOOM',
    'Online-chess',
    'Города',
    'GTA',
    'World of tanks'
]

together_games = get_together_games(anfisa_games, alisa_games)

for game in together_games:
    print("👾", game)
