from abc import ABC, abstractmethod


# ______________________________#______________________________#____________________________#

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

        # давайте метод для проверки цвета забабацаем
        @abstractmethod
        def color_validation(self, color):
            self.color = color.lower()
            if 'bl' in self.color or 'ck' in self.color:
                self.color = 'black'
                return color
            if 'w' in self.color or 'wh':
                self.color = 'white'
                return self.color

    # _________________________________________________________________________________

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
                        row_display.append(f' {piece.get_color()[0].upper()} ')
                print(' '.join(row_display))
            print()



    # Абстрактные классы готовы,теперь нужно пррогнать программу и потестить
    test_figure = Rook('black')
    print(f"Цвет: {test_figure.get_color()}, тип фигуры {test_figure.__class__.__name__}")

    test_figure = Rook('white')
    print(f"Цвет: {test_figure.get_color()}, тип фигуры {test_figure.__class__.__name__}")

    test_figure = Pawn('blck')
    print(f"Цвет: {test_figure.get_color()}, тип фигуры {test_figure.__class__.__name__}")

    test_figure = Pawn('wh')
    print(f"Цвет: {test_figure.get_color()}, тип фигуры {test_figure.__class__.__name__}")

    board = Chess_board()
    print("Initial Board:")
    Chess_board.display_board(board.get_field())

    print("Белые фигуры:", Chess_board.count_pieces(board.get_field(), 'white'))
    print("черные фигуры:", Chess_board.count_pieces(board.get_field(), 'black'))

    # итого: абстрактный класс и наследование есть, есть
    # есть обработка строк валидация
    # статические методы


if __name__ == "__main__":
    main()
