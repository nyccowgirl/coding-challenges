"""Given a chessboard with one K and one Q, see if the K can attack the Q.

This function is given coordinates for the king and queen on a chessboard.
These coordinates are given as a letter A-H for the columns and 1-8 for the
row (see below for example):

Queens can move in any direction: horizontally, vertically, or diagonally,
as far as possible.

This function returns True if the king is in the line of attack of the queen.

For example, these boards show the king under attack:

8    . . . . . . . .      . . . . . . . .      . . . . . . . .    8
7    . . . . . . . .      . . . . . . . .      . K . . . . . .    7
6    . . . K . . . Q      . . . . K . . .      . . . . . . . .    6
5    . . . . . . . .      . . . . . . . .      . . . Q . . . .    5
4    . . . . . . . .      . . . . Q . . .      . . . . . . . .    4
3    . . . . . . . .      . . . . . . . .      . . . . . . . .    3
2    . . . . . . . .      . . . . . . . .      . . . . . . . .    2
1    . . . . . . . .      . . . . . . . .      . . . . . . . .    1
     A B C D E F G H      A B C D E F G H      A B C D E F G H

     K=D6, Q=H6           K=E6, Q=E4           K=B7, Q=D5

>>> check("D6", "H6")
True

>>> check("E6", "E4")
True

>>> check("B7", "D5")
True

>>> check("A1", "H8")
True

>>> check("A8", "H1")
True

>>> check("D6", "H7")
False

>>> check("E6", "F4")
False
"""


def check(king, queen):
    """Given a chessboard with one K and one Q, see if the K can attack the Q.

    This function is given coordinates for the king and queen on a chessboard.
    These coordinates are given as a letter A-H for the columns and 1-8 for the
    row, like "D6" and "B7":
    """

    board = [['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8'],
             ['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7'],
             ['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6'],
             ['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5'],
             ['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4'],
             ['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3'],
             ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2'],
             ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1']]

    king = [(i, position.index(king)) for i, position in enumerate(board) if king in position]
    queen = [(i, position.index(queen)) for i, position in enumerate(board) if queen in position]

    if king[0][0] == queen[0][0]:
        return True
    elif king[0][1] == queen[0][1]:
        return True
    elif (king[0][0] - queen[0][0]) == (king[0][1] - queen[0][1]):
        return True
    elif (king[0][0] - queen[0][0]) == (queen[0][1] - king[0][1]):
        return True
    else:
        return False


# SOLUTION FILE:

# def check(king, queen):
#     """Given a chessboard with one K and one Q, see if the K can attack the Q.

#     This function is given coordinates for the king and queen on a chessboard.
#     These coordinates are given as a letter A-H for the columns and 1-8 for the
#     row, like "D6" and "B7":
#     """

#     # START SOLUTION

#     king_col = col_to_num(king[0])
#     king_row = int(king[1])

#     queen_col = col_to_num(queen[0])
#     queen_row = int(queen[1])

#     # Easy check: on same row or column

#     if king_col == queen_col or king_row == queen_row:
#         return True

#     # Diagonal check

#     return abs(king_col - queen_col) == abs(king_row - queen_row)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. EXCELLENT GAME!\n"
