# BASIC SUDOKU WITH BACKTRACKING ALGORITHM


def greeting():
    """Displays greeting to the game."""

    print "Let's solve Sudoku!"


def instructions():
    """Displays position numbers for board.

    Board index positions are as follows:
        0,0|0,1|0,2||0,3|0,4|0,5||0,6|0,7|0,8
        ---|---|---||---|---|---||---|---|---
        1,0|1,1|1,2||1,3|1,4|1,5||1,6|1,7|1,8
        ---|---|---||---|---|---||---|---|---
        2,0|2,1|2,2||2,3|2,4|2,5||2,6|2,7|2,8
        ===|===|===++===|===|===++===|===|===
        3,0|3,1|3,2||3,3|3,4|3,5||3,6|3,7|3,8
        ---|---|---||---|---|---||---|---|---
        4,0|4,1|4,2||4,3|4,4|4,5||4,6|4,7|4,8
        ---|---|---||---|---|---||---|---|---
        5,0|5,1|5,2||5,3|5,4|5,5||5,6|5,7|5,8
        ===|===|===++===|===|===++===|===|===
        6,0|6,1|6,2||6,3|6,4|6,5||6,6|6,7|6,8
        ---|---|---||---|---|---||---|---|---
        7,0|7,1|7,2||7,3|7,4|7,5||7,6|7,7|7,8
        ---|---|---||---|---|---||---|---|---
        8,0|8,1|8,2||8,3|8,4|8,5||8,6|8,7|8,8
    """

    s = '|'
    ds = '||'
    dp = '++'

    print '\nThe following are the position numbers on the board:\n'
    print 'A1 ' + s + 'A2 ' + s + 'A3 ' + ds + 'A4 ' + s + 'A5 ' + s + 'A6 ' + ds + 'A7 ' + s + 'A8 ' + s + 'A9 '
    print '---' + s + '---' + s + '---' + ds + '---' + s + '---' + s + '---' + ds + '---' + s + '---' + s + '---'
    print 'B1 ' + s + 'B2 ' + s + 'B3 ' + ds + 'B4 ' + s + 'B5 ' + s + 'B6 ' + ds + 'B7 ' + s + 'B8 ' + s + 'B9 '
    print '---' + s + '---' + s + '---' + ds + '---' + s + '---' + s + '---' + ds + '---' + s + '---' + s + '---'
    print 'C1 ' + s + 'C2 ' + s + 'C3 ' + ds + 'C4 ' + s + 'C5 ' + s + 'C6 ' + ds + 'C7 ' + s + 'C8 ' + s + 'C9 '
    print '===' + s + '===' + s + '===' + dp + '===' + s + '===' + s + '===' + dp + '===' + s + '===' + s + '==='
    print 'D1 ' + s + 'D2 ' + s + 'D3 ' + ds + 'D4 ' + s + 'D5 ' + s + 'D6 ' + ds + 'D7 ' + s + 'D8 ' + s + 'D9 '
    print '---' + s + '---' + s + '---' + ds + '---' + s + '---' + s + '---' + ds + '---' + s + '---' + s + '---'
    print 'E1 ' + s + 'E2 ' + s + 'E3 ' + ds + 'E4 ' + s + 'E5 ' + s + 'E6 ' + ds + 'E7 ' + s + 'E8 ' + s + 'E9 '
    print '---' + s + '---' + s + '---' + ds + '---' + s + '---' + s + '---' + ds + '---' + s + '---' + s + '---'
    print 'F1 ' + s + 'F2 ' + s + 'F3 ' + ds + 'F4 ' + s + 'F5 ' + s + 'F6 ' + ds + 'F7 ' + s + 'F8 ' + s + 'F9 '
    print '===' + s + '===' + s + '===' + dp + '===' + s + '===' + s + '===' + dp + '===' + s + '===' + s + '==='
    print 'G1 ' + s + 'G2 ' + s + 'G3 ' + ds + 'G4 ' + s + 'G5 ' + s + 'G6 ' + ds + 'G7 ' + s + 'G8 ' + s + 'G9 '
    print '---' + s + '---' + s + '---' + ds + '---' + s + '---' + s + '---' + ds + '---' + s + '---' + s + '---'
    print 'H1 ' + s + 'H2 ' + s + 'H3 ' + ds + 'H4 ' + s + 'H5 ' + s + 'H6 ' + ds + 'H7 ' + s + 'H8 ' + s + 'H9 '
    print '---' + s + '---' + s + '---' + ds + '---' + s + '---' + s + '---' + ds + '---' + s + '---' + s + '---'
    print 'I1 ' + s + 'I2 ' + s + 'I3 ' + ds + 'I4 ' + s + 'I5 ' + s + 'I6 ' + ds + 'I7 ' + s + 'I8 ' + s + 'I9 '


def draw_board(board):
    """Draws board. Value of 0 in any position indicates empty cell.

    Board index positions are as follows:
        0,0|0,1|0,2||0,3|0,4|0,5||0,6|0,7|0,8
        ---|---|---||---|---|---||---|---|---
        1,0|1,1|1,2||1,3|1,4|1,5||1,6|1,7|1,8
        ---|---|---||---|---|---||---|---|---
        2,0|2,1|2,2||2,3|2,4|2,5||2,6|2,7|2,8
        ===|===|===++===|===|===++===|===|===
        3,0|3,1|3,2||3,3|3,4|3,5||3,6|3,7|3,8
        ---|---|---||---|---|---||---|---|---
        4,0|4,1|4,2||4,3|4,4|4,5||4,6|4,7|4,8
        ---|---|---||---|---|---||---|---|---
        5,0|5,1|5,2||5,3|5,4|5,5||5,6|5,7|5,8
        ===|===|===++===|===|===++===|===|===
        6,0|6,1|6,2||6,3|6,4|6,5||6,6|6,7|6,8
        ---|---|---||---|---|---||---|---|---
        7,0|7,1|7,2||7,3|7,4|7,5||7,6|7,7|7,8
        ---|---|---||---|---|---||---|---|---
        8,0|8,1|8,2||8,3|8,4|8,5||8,6|8,7|8,8
    """
    s = '|'
    ds = '||'
    dp = '++'

    print (board[0][0] + s + board[0][1] + s + board[0][2] + ds +
           board[0][3] + s + board[0][4] + s + board[0][5] + ds +
           board[0][6] + s + board[0][7] + s + board[0][8])
    print ('---' + s + '---' + s + '---' + ds +
           '---' + s + '---' + s + '---' + ds +
           '---' + s + '---' + s + '---')
    print (board[1][0] + s + board[1][1] + s + board[1][2] + ds +
           board[1][3] + s + board[1][4] + s + board[1][5] + ds +
           board[1][6] + s + board[1][7] + s + board[1][8])
    print ('---' + s + '---' + s + '---' + ds +
           '---' + s + '---' + s + '---' + ds +
           '---' + s + '---' + s + '---')
    print (board[2][0] + s + board[2][1] + s + board[2][2] + ds +
           board[2][3] + s + board[2][4] + s + board[2][5] + ds +
           board[2][6] + s + board[2][7] + s + board[2][8])
    print ('===' + s + '===' + s + '===' + dp +
           '===' + s + '===' + s + '===' + dp +
           '===' + s + '===' + s + '===')
    print (board[3][0] + s + board[3][1] + s + board[3][2] + ds +
           board[3][3] + s + board[3][4] + s + board[3][5] + ds +
           board[3][6] + s + board[3][7] + s + board[3][8])
    print ('---' + s + '---' + s + '---' + ds +
           '---' + s + '---' + s + '---' + ds +
           '---' + s + '---' + s + '---')
    print (board[4][0] + s + board[4][1] + s + board[4][2] + ds +
           board[4][3] + s + board[4][4] + s + board[4][5] + ds +
           board[4][6] + s + board[4][7] + s + board[4][8])
    print ('---' + s + '---' + s + '---' + ds +
           '---' + s + '---' + s + '---' + ds +
           '---' + s + '---' + s + '---')
    print (board[5][0] + s + board[5][1] + s + board[5][2] + ds +
           board[5][3] + s + board[5][4] + s + board[5][5] + ds +
           board[5][6] + s + board[5][7] + s + board[5][8])
    print ('===' + s + '===' + s + '===' + dp +
           '===' + s + '===' + s + '===' + dp +
           '===' + s + '===' + s + '===')
    print (board[6][0] + s + board[6][1] + s + board[6][2] + ds +
           board[6][3] + s + board[6][4] + s + board[6][5] + ds +
           board[6][6] + s + board[6][7] + s + board[6][8])
    print ('---' + s + '---' + s + '---' + ds +
           '---' + s + '---' + s + '---' + ds +
           '---' + s + '---' + s + '---')
    print (board[7][0] + s + board[7][1] + s + board[7][2] + ds +
           board[7][3] + s + board[7][4] + s + board[7][5] + ds +
           board[7][6] + s + board[7][7] + s + board[7][8])
    print ('---' + s + '---' + s + '---' + ds +
           '---' + s + '---' + s + '---' + ds +
           '---' + s + '---' + s + '---')
    print (board[8][0] + s + board[8][1] + s + board[8][2] + ds +
           board[8][3] + s + board[8][4] + s + board[8][5] + ds +
           board[8][6] + s + board[8][7] + s + board[8][8])


def input_board():
    """Obtains user's input of sudoku puzzle to solve."""

    row = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    coll = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    print ('\nInput values in each position of the puzzle you want to solve. '
           'Enter 0 for empty positions. Enter Q to quit/escape.\n')

    while True:
        board = []

        for x in range(len(row)):
            temp = []
            for y in range(len(coll)):

                #
                while True:
                    num = raw_input('Value at ' + row[x] + coll[y] + ' : ')

                    # Validates that input is integer between 1- 9
                    if num.upper() == 'Q':
                        break
                    elif not isinstance(int(num), int):
                        print 'input is not a number'
                    elif (int(num) < 0) or (int(num) > 9):
                        print 'input is not between 0 and 9'
                    elif (int(num) != 0) and (int(num) in temp):
                        print 'number has already been inputted for the row'

                temp.append(int(num))
            board.append(temp)

        print '\nThe puzzle that was inputted is:\n'

        draw_board(board)

        while True:
            # User to confirm accuracy of puzzle
            confirm = raw_input('\nIs this accurate? (Y/N) ')
            confirm = confirm.upper()

            if confirm not in ['Y', 'N']:
                print 'Please input Y or N!'
            else:
                break

        if confirm == 'Y':
            break

    return board


def find_next(board, ridx, cidx):
    """Find next empty position."""

    for x in range(ridx, 9):
        for y in range(cidx, 9):
            if board[x][y] == 0:
                return x, y

    # Returns (-1, -1) if board is filled

    return -1, -1


def is_valid(board, ridx, cidx, guess):
    """Checks if guess is valid input for cell."""

    chk_row = all([guess != board[ridx][y] for y in range(9)])

    if chk_row:
        chk_coll = all([guess != board[x][cidx] for x in range(9)])
        if chk_coll:
            # Determines the top left of 3x3 section that contains the ridx, cidx cell
            secx, secy = 3 * (ridx / 3), 3 * (cidx / 3)  # floor/integer division

            for x in range(secx, secx + 3):
                for y in range(secy, secy + 3):
                    if board[x][y] == guess:
                        return False

            return True

    return False


def solve(board, ridx=0, cidx=0):
    """Solve puzzle."""

    ridx, cidx = find_next(board, ridx, cidx)

    if ridx == -1:
        return True

    for guess in range(1, 10):
        if is_valid(board, ridx, cidx, guess):
            board[ridx][cidx] = guess

            # Recurse until puzzle is filled
            if solve(board, ridx, cidx):
                return True

            # Undo current cell for backtracking
            board[ridx][cidx] = 0

    return False


def play_again():
    """Obtains user's input to solve another puzzle."""

    while True:
        repeat = raw_input('Do you want to solve another puzzle? (Y/N) ')

        repeat = repeat.upper()

        if repeat not in ['Y', 'N']:
            print 'Please input Y or N!'
        elif repeat == 'Y':
            return True
            break
        else:
            return False
            break


def execute_repl():
    """Executes sudoku solver."""

    greeting()

    while True:
        instructions()

        # Obtain puzzle from user to solve
        puzzle = input_board()

        solution = solve(puzzle)

        if not solution:
            print 'No viable solution'
        else:
            draw_board(puzzle)

        if not play_again():
            break


################################################################################

if __name__ == '__main__':

    execute_repl()
