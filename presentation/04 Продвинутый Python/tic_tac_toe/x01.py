# game.py
# Объявить класс.
class Board:
    # Инициализировать игровое поле - список списков с пробелами.
    # Пробелы - это пустые клетки.
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    # Метод, который обрабатывает ходы игроков.
    def make_move(self, row, col, player):
        self.board[row][col] = player
 
    # Метод, который отрисовывает игровое поле.
    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)


# Создать игровое поле - объект класса Board.
game = Board()
# Отрисовать поле в терминале.
game.display()
# Разместить на поле символ по указанным координатам - сделать ход.
game.make_move(1, 1, 'X')
print('Ход сделан!')
# Перерисовать поле с учётом сделанного хода.
game.display()







# Создайте в директории проекта tic_tac_toe новый файл, назовите его parts.py.
# Перенесите из файла game.py в файл parts.py класс с описанием игрового поля и сохраните изменения:
# parts.py
class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)


# Теперь задействуйте код из нового файла в своей программе. 
# Основной код игры вы продолжите писать в файле game.py.
# Файл с основным кодом программы часто называют исполняемым скриптом.
# Импортируйте в него класс Board из файла parts.py:
# game.py

from parts import Board

game = Board()
game.display()
game.make_move(1, 1, 'X')
print('Ход сделан!')
game.display() 










# Теперь превратите обычную папку в пакет — внутри каталога создайте файл __init__.py.
# Также переместите в каталог gameparts/ файл parts.py.
# Структура вашей программы должна быть такой:
tic_tac_toe/
├── gameparts/
│  ├── __init__.py
│  └── parts.py
├── venv/
└── game.py 




# Добавьте в файл __init__.py общий для всех файлов пакета gameparts/ импорт:
# gameparts/__init__.py.

# gameparts/__init__.py.
# Точка в записи означает текущий каталог.
from .parts import Board 


# Пакет готов к использованию! Перейдите в файл game.py и импортируйте в него класс Board из пакета gameparts/.
# Замените этот импорт…

# game.py
from gameparts.parts import Board
# …на новый:
from gameparts import Board

... 

# Хоть в вашей программе и появился собственный модуль и даже пакет, всё должно отработать без изменений











# Обычно разработчики выносят код, который должен выполняться при запуске исполняемого скрипта,
# в отдельную функцию, а потом обращаются к этой функции в блоке if __name__ == '__main__'.
# Чаще всего такую функцию называют main().

# Доработайте код в файле game.py:
# game.py

from gameparts import Board

# Вот новая функция.
def main():
    game = Board()
    game.display()
    game.make_move(1, 1, 'X')
    print('Ход сделан!')
    game.display()

# А вот вызов этой функции.
if __name__ == '__main__':
    main() 









# Пусть при вызове STR выводится строка Объект игрового поля размером 3x3.
# Размер поля лучше вынести в атрибут класса и задействовать его при формировании нужной строки.
# В коде файла parts.py переопределите метод __str__:
# gameparts/parts.py

class Board:

    # Новый атрибут.
    field_size = 3

    def __init__(self):
        self.board = [
            [' ' for _ in range(self.field_size)] for _ in range(self.field_size)
        ]

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    # Переопределяем метод __str__.
    def __str__(self):
        return (
            'Объект игрового поля размером '
            f'{self.field_size}x{self.field_size}'
        )
    





# Добавьте в описание класса в модуле parts.py докстринг.
# gameparts/parts.py

class Board:
    """Класс, который описывает игровое поле."""

    field_size = 3

    def __init__(self):
        self.board = [
            [' ' for _ in range(self.field_size)] for _ in range(self.field_size)
        ]

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def __str__(self):
        return (
            'Объект игрового поля размером '
            f'{self.field_size}x{self.field_size}'
        )
# Теперь, чтобы узнать подробности о классе Board, достаточно будет выполнить команду:
...




print(Board.__doc__)

# Выведется:
# Класс, который описывает игровое поле. 









# ИСКЛЮЧЕНИЯ

# Дополните код игры возможностью вводить координаты ячейки для хода.
# Координаты — это номер строки и номер столбца.
# После того как координаты будут введены, они должны быть переданы в метод make_move().
# Внесите изменения в код в файле game.py: 
# game.py

from gameparts import Board

def main():
    game = Board()
    game.display()
    # Тут пользователь вводит координаты ячейки.
    row = int(input('Введите номер строки: '))
    column = int(input('Введите номер столбца: '))
    # В метод make_move передаются те координаты, которые ввёл пользователь.
    game.make_move(row, column, 'X')
    print('Ход сделан!')
    game.display()

if __name__ == '__main__':
    main()







# В директории gameparts/ создайте файл exceptions.py и добавьте в него код собственного исключения с именем FieldIndexError.
# Это исключение будет унаследовано от подкласса IndexError.
# gameparts/exceptions.py

class FieldIndexError(IndexError):

    def __str__(self):
        return 'Введено значение за границами игрового поля'
    



# Некорректный ввод пользователя будет обрабатываться в файле game.py. Допишите код в нём:
# game.py

from gameparts import Board
# Из файла exceptions.py, который лежит в пакете gameparts,
# импортируется класс FieldIndexError.
from gameparts.exceptions import FieldIndexError


def main():
    game = Board()
    game.display()
    # Пользователь вводит номер строки.
    row = int(input('Введите номер строки: '))
    # Если введённое значение меньше нуля или больше или равно
    # field_size (это значение равно трём, оно хранится в модуле
    # parts.py)...
    if row < 0 or row >= game.field_size:
        # ...выбросить исключение FieldIndexError.
        raise FieldIndexError
    column = int(input('Введите номер столбца: '))
    
    game.make_move(row, column, 'X')
    print('Ход сделан!')
    game.display()

if __name__ == '__main__':
    main()



# Теперь запустите программу и введите значение 3 для строки. В терминал должна вывестись подобная информация:
# Traceback (most recent call last):
#   File "/Users/practicum/dev/tic_tac_toe/game.py", line 19, in <module>
#     raise FieldIndexError
#     gameparts.exceptions.FieldIndexError: Введено значение за границами игрового поля





# ЗАДАНИЕ. 
# Добавьте аналогичную обработку исключения для номера столбца — значения column.








# Обработка исключения для номера столбца должна выглядеть так:

# game.py

...

    column = int(input('Введите номер столбца: '))
    if column < 0 or column >= game.field_size:
        raise FieldIndexError
   
    ...








# «Укрощение» исключений в игре «Крестики-нолики»
# Чтобы обработать ситуацию, когда пользователь вводит некорректные координаты ячейки,
# вам понадобится бесконечный цикл while.
# Он будет работать до тех пор, пока пользователь не введёт корректные значения координат игрового поля.
# Как только нужные значения будут введены, цикл завершится, и программа продолжит свою работу.

# Изучите код в листинге, внимательно прочтите комментарии и внесите изменения в файл game.py:
# game.py

from gameparts import Board
from gameparts.exceptions import FieldIndexError


def main():
    game = Board()
    game.display()

    # Запускается бесконечный цикл.
    while True:
        # В этом блоке содержатся операции, которые могут вызвать исключение.
        try:
            # Пользователь вводит значение номера строки.
            row = int(input('Введите номер строки: '))
            # Если введённое число меньше 0 или больше или равно game.field_size...
            if row < 0 or row >= game.field_size:
                # ...выбрасывается собственное исключение FieldIndexError.
                raise FieldIndexError
            column = int(input('Введите номер столбца: '))
            # Если введённое число меньше 0 или больше или равно game.field_size...
            if column < 0 or column >= game.field_size:
                # ...выбрасывается собственное исключение FieldIndexError.
                raise FieldIndexError
        # Если возникает исключение FieldIndexError...
        except FieldIndexError:
            # ...выводятся сообщения...
            print(
                'Значение должно быть неотрицательным и меньше '
                f'{game.field_size}.'
            )
            print('Пожалуйста, введите значения для строки и столбца заново.')
            # ...и цикл начинает свою работу сначала, предоставляя пользователю ещё одну попытку ввести данные.
            continue
        # Если в блоке try исключения не возникло...
        else:
            # ...значит, введённые значения прошли все проверки и могут быть использованы в дальнейшем.
            # Цикл прерывается.
            break

    game.make_move(row, column, 'X')
    print('Ход сделан!')
    game.display()


if __name__ == '__main__':
    main()









# Программа не ожидает, что вместо числа будет введено слово.
# Python выбросит встроенное исключение и прекратит работу программы.
# Чтобы этого избежать, нужно обработать ситуацию,
# если вдруг пользователь решит ввести номер столбца или строки буквами.
# 
# ЗАДАНИЕ. 
# Добавьте в блок except в файле game.py обработку исключения ValueError.
# В случае, если пользователь ввёл буквы, должно выводиться два сообщения:
# 1. Буквы вводить нельзя. Только числа.
# 2. Пожалуйста, введите значения для строки и столбца заново. 















# Код для обработки исключения ValueError должен получиться таким:
# game.py

...

except ValueError:
    print('Буквы вводить нельзя. Только числа.')
    print('Пожалуйста, введите значения для строки и столбца заново.')
    continue

... 










# Также Добавьте такую обработку в блок except в файле game.py
# Это обработка базового класса исключений, которую обычно добавляют после обработки конкретных, ожидаемых исключений. 
# game.py

# ...

# except Exception as e:
    # print(f'Возникла ошибка: {e}')

# ...
