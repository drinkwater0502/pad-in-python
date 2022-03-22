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


def check_combos(board):
    # scan for 3+ more in each direction of each orb

    h_matches = check_rows(board)
    v_matches = check_columns(board)

    groups_to_remove = [] # groups of combos that need to be broken 

    # for hkey in h_matches:
    #     # hkey is the nth row of the board (ex: the '3' in 3:[4, 5, 6])
    #     if h_matches[hkey] != 0: # if any matches exist in that row
    #         for x in h_matches[hkey]: # for each x value in that row
    #             for vkey in v_matches:
    #                 if vkey == x:
    #                     for y in v_matches[vkey]:
    #                         if y == hkey:
    #                             group = [h_matches[hkey], v_matches[vkey]]

    



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
    new_board = start_board() #new_board = string of 30 characters
    print(GUI_board(new_board))
    print(check_rows(new_board))
    print(check_columns(new_board))

main()