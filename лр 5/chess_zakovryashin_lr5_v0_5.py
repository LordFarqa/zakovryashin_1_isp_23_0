import random
import tkinter as tk
from tkinter import messagebox
from abc import ABC, abstractmethod
from random import randint as rand
import logging
from datetime import datetime

logging.basicConfig(filename='chess_game.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def log_action(message):
    logging.info(message)


def main():
    class ChessError(Exception):
        """Основная ошибка"""
        pass

    class InvalidMoveError(ChessError):
        """Исключение, возникающее при попытке осуществить недопустимый ход."""
        def __init__(self, message="Недопустимый ход"):
            self.message = message
            super().__init__(self.message)

    class PieceNotSelectedError(ChessError):
        """Исключение, возникающее, когда игрок пытается переместить фигуру, не выбрав ее."""
        def __init__(self, message="Фигура не выбрана"):
            self.message = message
            super().__init__(self.message)

    class OutOfBoundsError(ChessError):
        """Исключение, возникающее при выходе за пределы доски."""
        def __init__(self, message="Выход за пределы доски"):
            self.message = message
            super().__init__(self.message)

    class InvalidColorError(ChessError):
        """Исключение, возникающее при попытке создать фигуру с недопустимым цветом."""
        def __init__(self, message="Недопустимый цвет фигуры"):
            self.message = message
            super().__init__(self.message)

    class Figure(ABC):
        def __init__(self, color):
            self.color = self.color_validation(color)

        @abstractmethod
        def can_move(self, board, row, column, row1, column1):
            return True

        @abstractmethod
        def can_attack(self, board, row, column, row1, column1):
            return self.can_move(board, row, column, row1, column1)

        @abstractmethod
        def get_color(self):
            return self.color

        def color_validation(self, color):
            color = color.lower()
            if 'bl' in color or 'ck' in color:
                return 'black'
            if 'w' in color or 'wh' in color:
                return 'white'
            raise InvalidColorError()



    class Rook(Figure):
        def __init__(self, color):
            super().__init__(color)
            log_action(f"Creating {self}.")

        def can_move(self, board, row, column, row1, column1):
            return row == row1 or column == column1

        def can_attack(self, board, row, column, row1, column1):
            return self.can_move(board, row, column, row1, column1)

        def get_color(self):
            return super().get_color()

        def __str__(self):
            return f"Rook(color='{self.color}')"

        def __repr__(self):
            return f"Rook(color='{self.color}')"

    def on_square_click(self, row, col):
        try:
            log_action(f"Square clicked: {row}, {col}.")
        except ChessError as e:
            log_action(f"Error: {e.message}")
    class Pawn(Figure):
        def __init__(self, color):
            super().__init__(color)

        def can_move(self, board, row, column, row1, column1):
            return True

        def can_attack(self, board, row, column, row1, column1):
            return True

        def get_color(self):
            return super().get_color()

    class Queen(Figure):
        def __init__(self, color):
            super().__init__(color)

        def can_move(self, board, row, column, row1, column1):
            return True

        def can_attack(self, board, row, column, row1, column1):
            return True

        def get_color(self):
            return super().get_color()

    class Bishop(Figure):
        def __init__(self, color):
            super().__init__(color)

        def can_move(self, board, row, column, row1, column1):
            return abs(row - row1) == abs(column - column1)

        def can_attack(self, board, row, column, row1, column1):
            return self.can_move(board, row, column, row1, column1)

        def get_color(self):
            return super().get_color()

    class King(Figure):
        def __init__(self, color):
            super().__init__(color)

        def can_move(self, board, row, column, row1, column1):
            return max(abs(row - row1), abs(column - column1)) == 1

        def can_attack(self, board, row, column, row1, column1):
            return self.can_move(board, row, column, row1, column1)

        def get_color(self):
            return super().get_color()


    class Hourse(Figure):
        def __init__(self, color):
            super().__init__(color)

        def can_move(self, board, row, column, row1, column1):
            return (abs(row - row1), abs(column - column1)) in [(2, 1), (1, 2)]

        def can_attack(self, board, row, column, row1, column1):
            return self.can_move(board, row, column, row1, column1)

        def get_color(self):
            return super().get_color()

    class Chess_board:
        total_pieces = 32
        created_boards = 0

        def __init__(self):
            self.color = 'WHITE'
            self.field = [[None] * 8 for _ in range(8)]
            self.field[0] = [
                Rook('WHITE'), Hourse('WHITE'), Bishop('WHITE'), Queen('WHITE'),
                King('WHITE'), Bishop('WHITE'), Hourse('WHITE'), Rook('WHITE')
            ]
            self.field[1] = [Pawn('WHITE')] * 8
            self.field[6] = [Pawn('BLACK')] * 8
            self.field[7] = [
                Rook('BLACK'), Hourse('BLACK'), Bishop('BLACK'), Queen('BLACK'),
                King('BLACK'), Bishop('BLACK'), Hourse('BLACK'), Rook('BLACK')
            ]
            Chess_board.created_boards += 1
            log_action("Creating a new chess board.")

        def get_board_type(self):
            try:
                b_type = input("введите тип доски: ")
                result = f'{b_type} Тип доски установлен'
                return result
            except Exception as e:
                print(f"Что-то пошло не по плану: {e}")
                raise
            finally:
                print("Завершение метода get_board_type.")

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
                    row_display.append(f' {piece.__class__.__name__.lower()} ' if piece else ' . ')
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
                new_board.field = self.get_field() + other.get_field()
                return new_board
            return NotImplemented

    class ChessApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Chess Game")
            self.board = Chess_board()
            self.buttons = [[None for _ in range(8)] for _ in range(8)]
            self.selected_piece = None
            self.selected_position = None
            self.create_board()

        def create_board(self):
            for row in range(8):
                for col in range(8):
                    color = "white" if (row + col) % 2 == 0 else "gray"
                    button = tk.Button(self.root, bg=color, width=6, height=3,
                                       command=lambda r=row, c=col: self.on_square_click(r, c))
                    button.grid(row=row, column=col)
                    self.buttons[row][col] = button
                    self.update_square(row, col)

        def update_square(self, row, col):
            piece = self.board.get_field()[row][col]
            self.buttons[row][col].config(text=piece.get_color()[0].upper() if piece else "")

        def on_square_click(self, row, col):
            try:
                piece = self.board.get_field()[row][col]
                if self.selected_piece is None:
                    if piece is not None:
                        self.selected_piece = piece
                        self.selected_position = (row, col)
                        print(f"Выбрано: {piece.get_color()} позиция {row}, {col}")
                    else:
                        raise PieceNotSelectedError("Выберите фигуру, чтобы сделать ход.")
                else:
                    if piece is None:
                        if not self.selected_piece.can_move(self.board.get_field(), self.selected_position[0],
                                                            self.selected_position[1], row, col):
                            raise InvalidMoveError("Этот ход недопустим для выбранной фигуры.")

                        self.board.get_field()[row][col] = self.selected_piece
                        self.board.get_field()[self.selected_position[0]][self.selected_position[1]] = None
                        self.update_square(row, col)
                        self.update_square(self.selected_position[0], self.selected_position[1])
                        self.selected_piece = None
                        self.selected_position = None
                    else:
                        print("Квадрат занят другой фигурой.")
            except IndexError:
                raise OutOfBoundsError("Выход за пределы доски.")
            except ChessError as e:
                print(f"Ошибка: {e.message}")
            except Exception as e:
                print(f"Произошла ошибка: {e}")
            finally:
                print(f"Обработка клика по квадрату завершена: {row}, {col}.")

    def filter_pieces_by_color(board, color):
        """Записыввем цвет фигур"""
        color = color.lower()
        pieces = []
        for row in board:
            for piece in row:
                if piece and piece.get_color() == color:
                    pieces.append(piece)
        return pieces

    def sort_pieces(pieces):
        """Сортируем фигуры по типу"""
        return sorted(pieces, key=lambda piece: piece.__class__.__name__)

    logging.basicConfig(filename='chess_game.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')







    chess_board = Chess_board()
    log_action("Доска создага")


    white_pieces = filter_pieces_by_color(chess_board.get_field(), 'white')
    sorted_white_pieces = sort_pieces(white_pieces)
    log_action(f"ОтФИльтрованы и отсортированы фигуры: {sorted_white_pieces}")


    root = tk.Tk()
    app = ChessApp(root)
    root.mainloop()
    rook = Rook('Black')
    log_action(f"Created a rook: {rook}")


    rook = Rook('Black')
    print(rook)
    print(repr(rook))


    new_rook = eval(repr(rook))
    print(new_rook)
# потом удалить
    def create_random_matrix():
        matrix = []
        for i in range(10):
            matrix_elem = []
            for j in range(random.randint(1, 10)):
                matrix_elem.append(random.randint(1, 2450))
            matrix.append(matrix_elem)
        return matrix

    matrix = create_random_matrix()

    def serch_elem_matrix(matrix):
        max_elem = 0
        if len(matrix) >= 1:
            for matrix_string in matrix:
                for elem in matrix_string:
                    if elem > max_elem:
                        max_elem = elem
            return max_elem
        return 0

if __name__ == "__main__":
    main()
