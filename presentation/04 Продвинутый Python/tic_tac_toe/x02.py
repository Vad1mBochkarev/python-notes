# Чтобы реализовать логику смены игрока, нужно доработать код в файле game.py следующим образом:
# 1.Добавить переменную, в которой по умолчанию будет храниться значение X,
# так как в игре «Крестики-нолики» первый ход обычно делают крестиками.
# Подходящее название для этой переменной — current_player.

# 2. Добавить флаговую переменную running со значением по умолчанию True.
# Она понадобится для управления основным циклом игры.
# Пока поднят флаг (running = True) — игра продолжается.
# Если флаг опущен (running = False) — цикл останавливается, и игра заканчивается.

# 3. Реализовать смену игроков. Эта возможность должна работать следующим образом:
# в каждой новой итерации цикла, если current_player равен X, новым значением будет O,
# иначе — новым значением будет X. Для реализации такого описания подойдёт тернарный оператор:
# current_player = 'O' if current_player == 'X' else 'X'.





# Изучите листинг и комментарии к нему, а затем доработайте код в файле game.py: 
# game.py

from gameparts import Board
from gameparts.exceptions import FieldIndexError


def main():
    game = Board()
    # Первыми ходят крестики.
    current_player = 'X'
    # Это флаговая переменная. По умолчанию игра запущена и продолжается.
    running = True
    game.display()
    # Тут запускается основной цикл игры.
    while running:
        print(f'Ход делают {current_player}')
        # Запускается бесконечный цикл для ввода координат игрового хода.
        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Введите значения для строки и столбца заново.')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Введите значения для строки и столбца заново.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break

        # Теперь для установки значения на поле само значение берётся
        # из переменной current_player.
        game.make_move(row, column, current_player)
        game.display()
        # Тернарный оператор, через который реализована смена игроков.
        # Если current_player равен X, то новым значением будет O,
        # иначе — новым значением будет X.
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()













# Чтобы игра шла по плану, нужно сделать так, чтобы программа не давала повторно записать значение в одну и ту же ячейку.
# То есть, если ячейка не пустая, программа должна выводить предупреждение и, например,
# предлагать повторно ввести координаты для хода. Для этого нужно описать ещё одно исключение.

# Создайте собственное исключение CellOccupiedError. Обновите код в файле exceptions.py:
# gameparts/exceptions.py

class FieldIndexError(IndexError):

    def __str__(self):
        return 'Введено значение за границами игрового поля'

# Вот оно - новое исключение, унаследованное от базового класса Exception.
class CellOccupiedError(Exception):

    def __str__(self):
        return 'Попытка изменить занятую ячейку'
    
# Теперь вы можете вызвать это исключение в основном коде игры. Обновите код в файле game.py:
# game.py

from gameparts import Board
# Добавился ещё один импорт - исключение CellOccupiedError.
from gameparts.exceptions import CellOccupiedError, FieldIndexError


def main():
    game = Board()
    current_player = 'X'
    running = True
    game.display()

    while running:
        print(f'Ход делают {current_player}')
        while True:  # Запускается бесконечный цикл.
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    # Вот тут выбрасывается новое исключение.
                    raise CellOccupiedError
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Введите значения для строки и столбца заново.')
                continue
            except CellOccupiedError:
                print('Ячейка занята')
                print('Введите другие координаты.')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Введите значения для строки и столбца заново.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break

        game.make_move(row, column, current_player)
        game.display()
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
# В игре «Крестики-нолики» сейчас реализовано всё, кроме главного:
# игра не завершается, когда кто-то из игроков побеждает или когда игра заканчивается ничьей.






# Чтобы определить ничью в игре, в класс Board в файле parts.py нужно добавить метод с вложенным циклом,
# который будет искать свободные ячейки. Если они есть, то игра продолжится, а если нет — завершится.

# Добавьте в класс Board в файле parts.py метод is_board_full() сразу после метода display():
# gameparts/parts.py
...

    def display(self):
        ...

    def is_board_full(self):
        # Цикл проходится по всем столбцам игрового поля.
        for i in range(self.field_size):
            # А потом по всем строчкам.
            for j in range(self.field_size):
                # Если находит свободную ячейку...
                if self.board[i][j] == ' ':
                    # ...игра продолжается.
                    return False
        # Иначе - ничья!
        return True

...





# Чтобы программа могла определить победу, нужно:

# 1.Реализовать проверку по вертикали и горизонтали с помощью цикла.
# Он будет проходиться по каждой строке и столбцу и проверять, одинаковые ли в них символы.


# 2. Реализовать проверку по диагонали с помощью условия.
# Нужно сравнить символы в определённых позициях поля.
# Например, для главной диагонали — это [0][0], [1][1], [2][2], а для побочной — [0][2], [1][1], [2][0].


# 3. В основном цикле игры после каждого хода нужно запускать
# обе проверки и если хотя бы одна из них закончится успешно,
# то опускать флаг running и выводить результат игры в терминал.

# Добавьте в класс Board в файле parts.py метод check_win() сразу после метода is_board_full():
# gameparts/parts.py

...

    # Этот метод будет определять победу.
    def check_win(self, player):
        # Тут реализована проверка по вертикали и горизонтали.
        for i in range(3):
            if (all([self.board[i][j] == player for j in range(3)]) or
                    all([self.board[j][i] == player for j in range(3)])):
                return True
        # Тут реализована проверка по диагонали.
        if (
            self.board[0][0] == self.board[1][1] == self.board[2][2] == player
            or
            self.board[0][2] == self.board[1][1] == self.board[2][0] == player
        ):
            return True
        return False

...
# И доработайте код в файле game.py:
# game.py

from gameparts import Board
from gameparts.exceptions import CellOccupiedError, FieldIndexError


def main():
    game = Board()
    current_player = 'X'
    running = True
    game.display()

    while running:

        print(f'Ход делают {current_player}')

        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise CellOccupiedError
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Введите значения для строки и столбца заново.')
                continue
            except CellOccupiedError:
                print('Ячейка занята.')
                print('Пожалуйста, введите другие координаты.')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Введите значения для строки и столбца заново.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break

        game.make_move(row, column, current_player)
        game.display()
        # После каждого хода надо делать проверку на победу и на ничью.
        if game.check_win(current_player):
            print(f'Победили {current_player}.')
            running = False
        elif game.is_board_full():
            print('Ничья!')
            running = False

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()







# ЗАПИСЬ В ФАЙЛ
# В директории tic_tac_toe создайте новый временный файл file_actions.py. В него вы добавите код, который:
# -откроет файл на запись,
# -добавит в него текст,
# -закроет файл.

# Для добавления текста можно использовать метод write().
# В качестве аргумента этому методу передаётся текст, который нужно записать в файл.
# Для переноса строк используются символы \n.
# file_actions.py

# Открыть на запись файл example.txt
file = open('example.txt', 'w', encoding='uft-8')
# Записать в файл строку.
file.write('Зевну, укроюсь с головою,\nбудильник заведу на март.\n')
# Закрыть файл.
file.close()

# Что изменилось в директории проекта?















# Как прочитать данные из файла
# Замените код в файле file_actions.py и запустите его:

# file_actions.py

# Открыть файл example.txt на чтение (аргумент 'r').
file = open('example.txt', 'r')
# Прочитать первые 12 символов из файла и сохранить их в переменную content.
content = file.read(12)
# Вывести на печать содержимое переменной content.
print(content)
# Закрыть файл.
file.close() 



# В терминале должны распечататься первые 12 символов из файла example.txt


# ЗАДАНИЕ
# Реализуйте в файле game.py запись результатов игр в файл.
# Если побеждают нолики, должна добавляться запись Победили 0.,
# если крестики — Победили Х., если случилась ничья — Ничья!.

# Для этого:
# 1. Добавьте в код функцию save_result().
# В ней должен открываться файл в режиме «добавление», чтобы информация в него не перезаписывалась после каждой игры,
# а добавлялась новой строкой. Назовите файл results.txt.

# 2. В часть программы, где определяется победитель или ничья (блок if game.check_win(current_player):),
# добавьте код, который будет формировать нужную строку и добавлять её в файл.
# Для этого нужно сформировать строку, сохранить её в переменную,
# затем вывести строку на печать и передать аргументом в функцию для записи в файл.


# Файлы file_actions.py и example.txt после больше не пригодятся, можете удалить их из папки проекта.










# А вот и итоговый код для файла game.py. Изучите решение и комментарии к нему. 
# game.py

from gameparts import Board
from gameparts.exceptions import CellOccupiedError, FieldIndexError


# Вот она - новая функция!
def save_result(result):
    # Открыть файл results.txt в режиме "добавление".
    # Если нужно явно указать кодировку, добавьте параметр encoding='utf-8'.
    file = open('results.txt', 'a', encoding='utf-8')
    # Записать в файл содержимое переменной result.
    file.write(result + '\n')
    file.close()


def main():
    game = Board()
    # Первыми ходят крестики.
    current_player = 'X'
    running = True
    game.display()

    while running:

        print(f'Ходит {current_player}')

        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise CellOccupiedError
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Введите значения для строки и столбца заново.')
                continue
            except CellOccupiedError:
                print('Ячейка занята.')
                print('Введите другие координаты.')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Введите значения для строки и столбца заново.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break

        game.make_move(row, column, current_player)
        game.display()
        if game.check_win(current_player):
            # Сформировать строку.
            result = f'Победили {current_player}.'
            # Вывести строку на печать.
            print(result)
            # Добавить строку в файл.
            save_result(result)
            running = False
        elif game.is_board_full():
            # Сформировать строку.
            result = 'Ничья!'
            # Вывести строку на печать.
            print(result)
            # Добавить строку в файл.
            save_result(result)
            running = False

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()


# Сыграйте партию в крестики-нолики до конца. После завершения игры в терминал должно вывестись сообщение о результатах,
# а также в папке tic_tac_toe должен появиться новый файл — results.txt.
# Если вы откроете этот файл, то увидите там результаты только что проведённой игры.
# Результаты следующих игр будут записываться новыми строками.







# Контекстный менеджер в игре
# ЗАДАНИЕ

# В коде игры «Крестики-нолики» реализуйте работу с файлом с помощью синтаксиса with … as ….
# Для этого переработайте код функции save_result() в файле game.py.








# Новая реализация функции save_result() должна быть такой:
# game.py
...

def save_result(result):
    # Если нужно явно указать кодировку, добавьте параметр encoding='utf-8'.
    with open('results.txt', 'a') as f:
        f.write(result + '\n')

...


# Программа будет работать как и прежде:
# после каждой новой игры результаты будут записываться в файл results.txt новой строкой.
