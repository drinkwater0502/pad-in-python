# initialize board
# orb pick-up and set down
# orb movement
# [ break combos <- 
# skyfall ] <-  repeat these as necessary


import math
import random


def check_rows(board):
    # top row is rows[0], bottom row is rows[4]
    rows = [[], [], [], [], []]
    for i in range(len(board)):
        if i >= 0 and i <= 5:
            rows[0].append(board[i])
        elif i >= 6 and i <= 11:
            rows[1].append(board[i])
        elif i >= 12 and i <= 17:
            rows[2].append(board[i])
        elif i >= 18 and i <= 23:
            rows[3].append(board[i])
        elif i >= 24 and i <= 29:
            rows[4].append(board[i])
    matches = {}
    for row_idx in range(len(rows)): # for each row in rows
        row_matches = [] # store matches (including dupes) in here
        for orb_idx in range(1, 5): # for each orb in that row (excluding the first and last orb)
            if rows[row_idx][orb_idx] == rows[row_idx][orb_idx + 1] and rows[row_idx][orb_idx] == rows[row_idx][orb_idx - 1]: # if the orb is the same as the one on its left and right
                row_matches.extend([orb_idx - 1, orb_idx, orb_idx + 1]) # append those indexes to row_matches
        row_matches = list(dict.fromkeys(row_matches)) # unique matches in that row
        matches[row_idx] = row_matches
    return matches

def check_columns(board):
    # leftmost column is columns[0], rightmost is columns[5]
    columns = [[], [], [], [], [], []]
    for i in range(len(board)):
        columns[i % 6].append(board[i])
    matches = {}
    for col_idx in range(len(columns)): # for each column in columns
        col_matches = [] # store matches (including dupes) in here
        for orb_idx in range(1, 4): # for each orb in that column (excluding the first and last orb)
            if columns[col_idx][orb_idx] == columns[col_idx][orb_idx + 1] and columns[col_idx][orb_idx] == columns[col_idx][orb_idx - 1]: # if the orb is the same as the one above and below it
                col_matches.extend([orb_idx - 1, orb_idx, orb_idx + 1]) # append those indexes to col_matches
        col_matches = list(dict.fromkeys(col_matches)) # unique matches in that column
        matches[col_idx] = col_matches
    return matches

def above(idx):
    return idx - 6

def below(idx):
    return idx + 6

def left(idx):
    return idx - 1

def right(idx):
    return idx + 1

def check_combos(board):
    # scan for 3+ more in each direction of each orb

    r_group = []
    g_group = []
    b_group = []
    l_group = []
    d_group = []
    h_group = []
    h_dont_check = [4, 5, 10, 11, 16, 17, 22, 23, 28, 29]
    v_dont_check = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

    for square_idx in range(len(board)):
        matches = []
        if square_idx not in h_dont_check and board[square_idx] == board[right(square_idx)] and board[square_idx] == board[right(right(square_idx))]:
            matches.append(square_idx)
            matches.append(right(square_idx))
            matches.append(right(right(square_idx)))
            if board[square_idx] == 'r':
                r_group.extend(matches)
            elif board[square_idx] == 'g':
                g_group.extend(matches)
            elif board[square_idx] == 'b':
                b_group.extend(matches)
            elif board[square_idx] == 'd':
                d_group.extend(matches)
            elif board[square_idx] == 'l':
                l_group.extend(matches)
            elif board[square_idx] == 'h':
                h_group.extend(matches)
        if square_idx not in v_dont_check and board[square_idx] == board[below(square_idx)] and board[square_idx] == board[below(below(square_idx))]:
            matches.append(square_idx)
            matches.append(below(square_idx))
            matches.append(below(below(square_idx)))
            if board[square_idx] == 'r':
                r_group.extend(matches)
            elif board[square_idx] == 'g':
                g_group.extend(matches)
            elif board[square_idx] == 'b':
                b_group.extend(matches)
            elif board[square_idx] == 'd':
                d_group.extend(matches)
            elif board[square_idx] == 'l':
                l_group.extend(matches)
            elif board[square_idx] == 'h':
                h_group.extend(matches)
    
    r_group = list(dict.fromkeys(r_group))
    g_group = list(dict.fromkeys(g_group))
    b_group = list(dict.fromkeys(b_group))
    l_group = list(dict.fromkeys(l_group))
    d_group = list(dict.fromkeys(d_group))
    h_group = list(dict.fromkeys(h_group))

    print('r:', r_group)
    print('g:', g_group)
    print('b:', b_group)
    print('l:', l_group)
    print('d:', d_group)
    print('h:', h_group)

def group_combos(match_array):
    color_arr = []
    for i in range(len(match_array) - 1):
        if match_array[i + 1] - match_array[i] == 1:
            pass

def start_board():
    colors = ['r', 'g', 'b', 'l', 'd', 'h']
    board = []
    for i in range(30):
        board.append(random.choice(colors))
    return board

def GUI_board(board):
    toSend = ''
    for i in range(len(board)):
        toSend += board[i] + ' '
        if (i + 1) % 6 == 0:
            toSend += '\n'
    return toSend

def pick_up_orb(board):
    chosen = input('Select the orb to move: ')

def main():
    decision = input('Type in board or type r for a random board: ')
    if decision == 'r':
        new_board = start_board() #new_board = string of 30 characters
    else:
        new_board = decision.lower()
    print(GUI_board(new_board))
    print(check_rows(new_board))
    print(check_columns(new_board))
    check_combos(new_board)

main()