from random import randint

""" Test Board
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

clear_board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]
"""


# Solves board
def solve(sb):
    find = find_empty(sb)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, len(sb) + 1):
        if valid(sb, i, (row, col)):
            sb[row][col] = i

            if solve(sb):
                return True

            sb[row][col] = 0

    return False


# Validates an entered number
def valid(sb, num, pos):
    # Checking row
    for i in range(len(sb[0])):
        if sb[pos[0]][i] == num and pos[1] != i:
            return False

    # Checking column
    for j in range(len(sb)):
        if sb[j][pos[1]] == num and pos[0] != j:
            return False

    # Checking box

    box_row = pos[0] // 3
    box_col = pos[1] // 3

    for i in range(box_row * 3, (box_row * 3) + 3):
        for j in range(box_col * 3, (box_col * 3) + 3):
            if sb[i][j] == num and pos != (i, j):
                return False

    return True


# Displays board
def show_board(sb):
    for i in range(len(sb)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(sb[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(sb[i][j])
            else:
                print(str(sb[i][j]) + " ", end="")


# Finds first empty cell from top left
def find_empty(sb):
    for i in range(len(sb)):
        for j in range(len(sb[0])):
            if sb[i][j] == 0:
                return (i, j) # row and column

    return None


# Creates a randomly generated board
def rand_board(sb):
    num_randvalue = randint(1, 9)
    row_randvalue = randint(0, 8)
    col_randvalue = randint(0, 8)
    sb[row_randvalue][col_randvalue] = num_randvalue

    if valid(sb, num_randvalue, (row_randvalue, col_randvalue)) is False:
        sb[row_randvalue][col_randvalue] = 0
    else:
        if rand_board(sb):
            return True

    if non_zero(sb) < 18:
        rand_board(sb)


# Checks how many numbers are filled in
def non_zero(sb):
    count = 0
    for i in range(len(sb)):
        for j in range(len(sb[0])):
            if sb[i][j] != 0:
                count = count + 1

    return count

