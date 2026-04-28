# В директории tic_tac_toe создайте новый файл, назовите его pygame_test.py.
# Скопируйте в него код, задача которого — создать и открыть графическое окно,
# запустить цикл и отслеживать в нём единственно возможное действие пользователя
# — закрытие окна по нажатию кнопки выхода:
# pygame_test.py

# Импортировать библиотеку Pygame.
import pygame

# Инициализировать библиотеку Pygame.
pygame.init()

# Создать окно размером 800x600 точек (или пикселей).
screen = pygame.display.set_mode((800, 600))
# Задать окну заголовок.
pygame.display.set_caption('Пример графического окна Pygame')


running = True

# Описание главного цикла игры.
# Этот цикл работает до тех пор, пока пользователь не закроет окно.
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


# Деинициализирует все модули pygame, которые были инициализированы ранее.
pygame.quit()


# Запустите программу обычным для вас способом. Должно открыться окно.
# Всё, что можно сейчас сделать с этим окном, — это просто закрыть.





# Но при помощи Pygame можно ещё и отрисовать различные графические элементы, такие как линии или квадраты.

# Отсчёт координат ведётся с левого верхнего угла окна.
# Отрисуем эти элементы при помощи кода.
# pygame_test.py

# Импортировать библиотеку Pygame.
import pygame

# Инициализировать библиотеку Pygame.
pygame.init()

# Создать окно размером 800x600.
screen = pygame.display.set_mode((800, 600))
# Задать окну заголовок.
pygame.display.set_caption('Пример графического окна Pygame')


running = True

# Описание главного цикла игры.
# Этот цикл работает до тех пор, пока пользователь не закроет окно.
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Рисование линии.
    pygame.draw.line(screen, (255, 0, 0), (100, 100), (700, 500), 5)

    # Рисование квадрата.
    # Квадрат с верхним левым углом в точке (300, 200) и размерами 200x200 
    # будет нарисован зелёным цветом.
    pygame.draw.rect(screen, (0, 128, 0), pygame.Rect(300, 200, 200, 200))

    # Отобразить нарисованные элементы в окне.
    pygame.display.update()


# Деинициализирует все модули pygame, которые были инициализированы ранее.
pygame.quit()

# После запуска кода оба элемента будут отрисованы в графическом окне.






# ИТОГ
# Логика работы самой игры игры будет такой:
# - Отрисовываем графическое поле, запускаем главный цикл и ждём действий пользователя.
# - Пользователь может кликнуть по пустой клетке и в зависимости от того, чей ход, установить свой знак.
# - Ещё он может закончить игру, просто закрыв окно.

# Цикл игры будет работать пока не наступит ничью или победа.

# Метод display() больше не нужен.
# После каждого хода знаки на игровом поле можно отрисовать новой функцией draw_figures,
# а обновляться графическое окно будет в теле основного цикла.

# Написанные ранее собственные исключения теперь больше не понадобятся.
# Они были нужны для обработки ввода из терминала.
# Нет ввода — нет и исключений, которые могут возникнуть при этом вводе.

# ЗАДАНИЕ
# Перед вами листинг, где описана часть кода, которая будет отвечать за графический интерфейс игры «Крестики-нолики».
# Но в этом листинге не хватает логики игры, которую писали ранее.

# Прочитайте код, перенесите его в файл game.py и дополните недостающими блоками. В комментариях есть подсказки. 

# Метод display() из файла parts.py не понадобится для графической версии игры.
# Вместо него будет работать новая функция draw_figures().
# Если вы не планируете использовать консольный вариант игры, можете удалить или закомментировать метод display().
# game.py
import pygame
# Здесь нужно импортировать класс Board. Импорт исключений для игры
# с графическим интерфейсом не понадобится.
...
pygame.init()

# Здесь определены разные константы, например размер ячейки и доски, цвет и толщина линий.
# Эти константы используются при отрисовке графики. 
CELL_SIZE = 100
BOARD_SIZE = 3
WIDTH = HEIGHT = CELL_SIZE * BOARD_SIZE
LINE_WIDTH = 15
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
X_COLOR = (84, 84, 84)
O_COLOR = (242, 235, 211)
X_WIDTH = 15
O_WIDTH = 15
SPACE = CELL_SIZE // 4

# Настройка экрана.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Крестики-нолики')
# Заполнить фон окна заданным цветом.
screen.fill(BG_COLOR)

def draw_lines():
    # Горизонтальные линии.
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i * CELL_SIZE),
            (WIDTH, i * CELL_SIZE),
            LINE_WIDTH
        )
    # Вертикальные линии.
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * CELL_SIZE, 0),
            (i * CELL_SIZE, HEIGHT),
            LINE_WIDTH
        )
# Функция, которая отвечает за отрисовку фигур
def draw_figures(board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 'X':
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (col * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    X_WIDTH
                )
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (
                        col * CELL_SIZE + SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + SPACE
                    ),
                    X_WIDTH
                )
            elif board[row][col] == 'O':
                pygame.draw.circle(
                    screen,
                    O_COLOR,
                    (
                        col * CELL_SIZE + CELL_SIZE // 2,
                        row * CELL_SIZE + CELL_SIZE // 2
                    ),
                    CELL_SIZE // 2 - SPACE,
                    O_WIDTH
                )
# Сюда нужно добавить функцию save_result().
...
# В этой функции описана логика игры. Вам нужно её дополнить. По структуре 
# тут всё то же самое, что было в вашем коде раньше. 
# Но есть отличие - вместо метода display() используется новая функция draw_figures().
def main():
    game = Board()
    current_player = 'X'
    running = True
    draw_lines()

    # В цикле обрабатываются такие события, как нажатие кнопок мыши и закрытие окна.
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_y = event.pos[0]
                mouse_x = event.pos[1]
                clicked_row = mouse_x // CELL_SIZE
                clicked_col = mouse_y // CELL_SIZE
                if game.board[clicked_row][clicked_col] == ' ':  # если ячейка свободна,
                    # то сделать ход,
                    game.make_move(clicked_row, clicked_col, current_player)
                    # проверить на победу,
                    # проверить на ничью,
                    # сменить игрока. 
                    ...
                    draw_figures(game.board)
        pygame.display.update()
    # Деинициализирует все модули pygame, которые были инициализированы ранее.
    pygame.quit()


if __name__ == '__main__':
    main()






# РЕШЕНИЕ
# game.py

import pygame

from gameparts import Board

pygame.init()

CELL_SIZE = 100
BOARD_SIZE = 3
WIDTH = HEIGHT = CELL_SIZE * BOARD_SIZE
LINE_WIDTH = 15
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
X_COLOR = (84, 84, 84)
O_COLOR = (242, 235, 211)
X_WIDTH = 15
O_WIDTH = 15
SPACE = CELL_SIZE // 4

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Крестики-нолики')
screen.fill(BG_COLOR)

def draw_lines():
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i * CELL_SIZE),
            (WIDTH, i * CELL_SIZE),
            LINE_WIDTH
        )

    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * CELL_SIZE, 0),
            (i * CELL_SIZE, HEIGHT),
            LINE_WIDTH
        )

def draw_figures(board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 'X':
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (col * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    X_WIDTH
                )
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (
                        col * CELL_SIZE + SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + SPACE
                    ),
                    X_WIDTH
                )
            elif board[row][col] == 'O':
                pygame.draw.circle(
                    screen,
                    O_COLOR,
                    (
                        col * CELL_SIZE + CELL_SIZE // 2,
                        row * CELL_SIZE + CELL_SIZE // 2
                    ),
                    CELL_SIZE // 2 - SPACE,
                    O_WIDTH
                )

def save_result(result):
    # Если нужно явно указать кодировку, добавьте параметр encoding='utf-8'.
    with open('results.txt', 'a') as f:
        f.write(result + '\n')

def main():
    game = Board()
    current_player = 'X'
    running = True
    draw_lines()

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_y = event.pos[0]
                mouse_x = event.pos[1]

                clicked_row = mouse_x // CELL_SIZE
                clicked_col = mouse_y // CELL_SIZE

                if game.board[clicked_row][clicked_col] == ' ':
                    game.make_move(clicked_row, clicked_col, current_player)

                    if game.check_win(current_player):
                        result = f'Победили {current_player}.'
                        print(result)
                        save_result(result)
                        running = False
                    elif game.is_board_full():
                        result = 'Ничья!'
                        print(result)
                        save_result(result)
                        running = False

                    current_player = 'O' if current_player == 'X' else 'X'
                    draw_figures(game.board)

        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    main()