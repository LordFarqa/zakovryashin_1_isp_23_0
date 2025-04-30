from abc import ABC, abstractmethod

def main():
    class Figure(ABC):
        def __init__(self, color):
            self.color = color
            self.color_validation(color)

        @abstractmethod
        def can_move(self, board, row, column, row1, column1):
            return True

        @abstractmethod
        def can_attack(self, board, row, column, row1, column1):
            return self.can_move(board, row, column, row1, column1)

        @abstractmethod
        def get_color(self):
            return self.color

        @abstractmethod
        def color_validation(self, color):
            self.color = color.lower()
            if 'bl' in self.color or 'ck' in self.color:
                self.color = 'black'
                return color
            if 'w' in self.color or 'wh' in self.color:
                self.color = 'white'
                return self.color

    class Rook(Figure):
        def __init__(self, color):
            super().__init__(color)

        def can_move(self, board, row, column, row1, column1):
            return True

        def can_attack(self, board, row, column, row1, column1):
            return self.can_move(board, row, column, row1, column1)

        def get_color(self):
            return super().get_color()

        def color_validation(self, color):
            return super().color_validation(self.color)

    class Pawn(Figure):
        def __init__(self, color):
            super().__init__(color)

        def can_move(self, board, row, column, row1, column1):
            return True

        def can_attack(self, board, row, column, row1, column1):
            return self.can_move(board, row, column, row1, column1)

        def get_color(self):
            return super().get_color()

        def color_validation(self, color):
            return super().color_validation(self.color)

    class Queen(Figure):
        def __init__(self, color):
            super().__init__(color)

        def can_move(self, board, row, column, row1, column1):
            return True

        def can_attack(self, board, row, column, row1, column1):
            return self.can_move(board, row, column, row1, column1)

        def get_color(self):
            return super().get_color()

        def color_validation(self, color):
            return super().color_validation(self.color)

    class Bishop(Figure):
        def __init__(self, color):
            super().__init__(color)

        def can_move(self, board, row, column, row1, column1):
            return True

        def can_attack(self, board, row, column, row1, column1):
            return self.can_move(board, row, column, row1, column1)

        def get_color(self):
            return super().get_color()

        def color_validation(self, color):
            return super().color_validation(self.color)

    class King(Figure):
        def __init__(self, color):
            super().__init__(color)

        def can_move(self, board, row, column, row1, column1):
            return True

        def can_attack(self, board, row, column, row1, column1):
            return self.can_move(board, row, column, row1, column1)

        def get_color(self):
            return super().get_color()

        def color_validation(self, color):
            return super().color_validation(self.color)

    class Hourse(Figure):
        def __init__(self, color):
            super().__init__(color)

        def can_move(self, board, row, column, row1, column1):
            return True

        def can_attack(self, board, row, column, row1, column1):
            return self.can_move(board, row, column, row1, column1)

        def get_color(self):
            return super().get_color()

        def color_validation(self, color):
            return super().color_validation(self.color)

    class Chess_board:
        total_pieces = 32  # кол-во фигур
        created_boards = 0  #кол-во созданых досок

        def __init__(self):
            self.color = 'WHITE'
            self.field = []
            for row in range(8):
                self.field.append([None] * 8)
            self.field[0] = [
                Rook('WHITE'), Hourse('WHITE'), Bishop('WHITE'), Queen('WHITE'),
                King('WHITE'), Bishop('WHITE'), Hourse('WHITE'), Rook('WHITE')
            ]
            self.field[1] = [
                Pawn('WHITE'), Pawn('WHITE'), Pawn('WHITE'), Pawn('WHITE'),
                Pawn('WHITE'), Pawn('WHITE'), Pawn('WHITE'), Pawn('WHITE')
            ]
            self.field[6] = [
                Pawn('BLACK'), Pawn('BLACK'), Pawn('BLACK'), Pawn('BLACK'),
                Pawn('BLACK'), Pawn('BLACK'), Pawn('BLACK'), Pawn('BLACK')
            ]
            self.field[7] = [
                Rook('BLACK'), Hourse('BLACK'), Bishop('BLACK'), Queen('BLACK'),
                King('BLACK'), Bishop('BLACK'), Hourse('BLACK'), Rook('BLACK')
            ]
            Chess_board.created_boards += 1  # увеличиваем доски

        def get_board_type(self):
            b_type = input()
            result = f'{b_type} Тип доски установлен'
            return result

        def can_move(self, board, row, column, row1, column1):
            return True

        def can_attack(self, board, row, column, row1, column1):
            return self.can_move(board, row, column, row1, column1)

        def get_field(self):
            return self.field

        @staticmethod
        def count_pieces(board, color):
            count = 0
            for row in board:
                for piece in row:
                    if piece and piece.get_color() == color:
                        count += 1
            return count

        @staticmethod
        def display_board(board):
            for row in board:
                row_display = []
                for piece in row:
                    if piece is None:
                        row_display.append(' . ')
                    else:
                        row_display.append(f' {piece.__class__.__name__.lower()} ')
                print(' '.join(row_display))
            print()

        def __str__(self):
            return f" фигуры {Chess_board.total_pieces} и {Chess_board.created_boards} доски."

        def __eq__(self, other):
            if isinstance(other, Chess_board):
                return self.get_field() == other.get_field()
            return False

        def __add__(self, other):
            if isinstance(other, Chess_board):
                new_board = Chess_board()
                new_board.field = self.get_field() + other.get_field()  # сложение полей
                return new_board
            return NotImplemented

    # жесткая проверка

    test_figure = Rook('black')
    print(f"Цвет: {test_figure.get_color()}, тип фигуры {test_figure.__class__.__name__}")

    test_figure = Rook('white')
    print(f"Цвет: {test_figure.get_color()}, тип фигуры {test_figure.__class__.__name__}")

    test_figure = Pawn('blck')
    print(f"Цвет: {test_figure.get_color()}, тип фигуры {test_figure.__class__.__name__}")

    test_figure = Pawn('wh')
    print(f"Цвет: {test_figure.get_color()}, тип фигуры {test_figure.__class__.__name__}")

    board1 = Chess_board()
    print("Наша доска:")
    Chess_board.display_board(board1.get_field())

    print("Белые фигуры:", Chess_board.count_pieces(board1.get_field(), 'white'))
    print("черные фигуры:", Chess_board.count_pieces(board1.get_field(), 'black'))

    board2 = Chess_board()
    print("Создано досок:", Chess_board.created_boards)

    combined_board = board1 + board2  # доски сложили
    print(combined_board)  # информацию вывеоли жестко
    try:
        1 / 0
    except ZeroDivisionError as e:
        print(f'Исключение: {str(e)}')


if __name__ == "__main__":
    main()
