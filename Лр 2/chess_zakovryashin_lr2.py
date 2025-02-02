def main():
    class Rook:
        def __init__(self, color):
            self.color = color

        def can_move(self,board,row, column, row1, column1):
            return True

        def can_attack(self,board,row, column, row1, column1):
            return self.can_move(self,row,column,row1,column1)

        def get_color(self):
            return self.color

    class Pawn:
        def __init__(self, color):
            self.color = color

        def get_color(self):
            return self.color

        def can_move(self,board,row, column, row1, column1):
            return True

        def can_attack(self,board,row, column, row1, column1):
            return self.can_move(self,row,column,row1,column1)

    class Queen:
        def __init__(self, color):
            self.color = color

        def get_color(self):
            return self.color

        def can_move(self,board,row, column, row1, column1):
            return True

        def can_attack(self,board,row, column, row1, column1):
            return self.can_move(self,row,column,row1,column1)

    class Bishop:
        def __init__(self, color):
            self.color = color

        def get_color(self):
            return self.color
        def can_move(self,board,row, column, row1, column1):
            return True

        def can_attack(self,board,row, column, row1, column1):
            return self.can_move(self,row,column,row1,column1)

    class King:
        def __init__(self, color):
            self.color = color

        def get_color(self):
            return self.color

        def can_move(self,board,row, column, row1, column1):
            return True

        def can_attack(self,board,row, column, row1, column1):
            return self.can_move(self,row,column,row1,column1)

    class Hourse:
        def __init__(self, color):
            self.color = color

        def move(self):
            has_moved = False
            return has_moved

        def get_color(self):
            return self.color

        def can_move(self,board,row, column, row1, column1):
            return True

        def can_attack(self,board,row, column, row1, column1):
            return self.can_move(self,row,column,row1,column1)

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
            def get_board_type(board_type):
                b_type = input()
                result = f'{b_type} Тип доски установлен'
                return result

            def can_move(self, board, row, column, row1, column1):
                return True

            def can_attack(self, board, row, column, row1, column1):
                return self.can_move(self, row, column, row1, column1)


if __name__ == "__main__":
    main()
