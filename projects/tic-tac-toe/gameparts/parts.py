# Объявить класс.
class Board:
    # Инициализировать игровое поле - список списков с пробелами.
    # Пробелы - это пустые клетки.

    field_size = 3

    def __init__(self):
        self.board = [
            [' ' for _ in range(self.field_size)] for _ in range(self.field_size)
        ]

    # Метод, который обрабатывает ходы игроков.
    def make_move(self, row, col, player):
        self.board[row][col] = player

    # Метод, который отрисовывает игровое поле.
    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def __str__(self):
        return (
            'обьект игрового поля размером'
            f'{self.field_size}X{self.field_size}'
        )
    

    def is_board_full(self):
        for row in range(self.field_size):
            for colunm in range(self.field_size):
                if self.board[row][colunm] == ' ':
                    return False
        return True

    def is_ani_win(self):

        for i in range(0, 3):
            if self.board[i] == ['x', 'x', 'x'] or self.board[i] == ['o', 'o', 'o']:
                print(f'выйграл {self.board[i][1]}')
                return True
            elif self.board[0][i] == 'x' and self.board[1][i] == 'x' and self.board[2][i] == 'x':
                print('win x')
                return True
            elif self.board[0][i] == 'o' and self.board[1][i] == 'o' and self.board[2][i] == 'o':
                print('win o')
                return True
        if self.board[0][0] == 'x' and self.board[1][1] == 'x' and self.board[2][2] == 'x':
            print('win x')
            return True
        if self.board[0][0] == 'o' and self.board[1][1] == 'o' and self.board[2][2] == 'o':
            print('win o')
            return True
        
        
print(Board.__doc__)
