from gameparts.parts import Board
from gameparts.exceptions import FieldIndexError, CellOccupiedError


def main():
    game = Board()

    current_player = "x"

    running = True

    game.display()

    logs = open('logs.txt', 'a', encoding='utf-8')

    def now_result():

        logs.write(f'{current_player} ходил в {row}, {column}\n')

        now_board = ' \n-----\n'.join('|'.join(row) for row in game.board)

        logs.write(f'после этого поле выглядит так:\n{now_board}\n\n')

    while running:

        print(f"сейчас. ходит {current_player}")

        while True:

            try:
                row = int(input('Введите номер строки: '))
                if row <= 0 or row >= game.field_size + 1:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column <= 0 or column >= game.field_size + 1:
                    raise FieldIndexError
                
                if game.board[row - 1][column - 1] != ' ':
                    raise CellOccupiedError
                
                game.make_move(row - 1, column - 1, current_player)
                print('Ход сделан!')
                game.display()
            except FieldIndexError:
                print('Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.')
                print('Пожалуйста, введите значения для строки и столбца заново.')
                continue
            finally:

                if game.is_ani_win() == True:
                    now_result()
                    logs.write(f'{current_player} победил!\n')
                    break

                if game.is_board_full() == True:
                    now_result()
                    logs.write(f'Ничья!\n')
                    break

                now_result()

                current_player = 'o' if current_player == 'x' else 'x'

        break


    
if __name__ == "__main__":
    main()


    