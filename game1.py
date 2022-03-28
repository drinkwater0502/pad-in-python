import random

def start_board():
    colors = ['r', 'g', 'b', 'l', 'd', 'h']
    board = [[], [], [], [], []]
    for row in board:
        for i in range(6):
            row.append(random.choice(colors))
    return board

def gui_board(board):
    for row in board:
        print(row)

def two_dimension(orb_string):
    
    board = [[], [], [], [], []]
    for orb_idx in range(len(orb_string)):
        if orb_idx <= 5:
            board[0].append(orb_string[orb_idx])
        elif orb_idx > 5 and orb_idx <= 11:
            board[1].append(orb_string[orb_idx])
        elif orb_idx > 11 and orb_idx <= 17:
            board[2].append(orb_string[orb_idx])
        elif orb_idx > 17 and orb_idx <= 23:
            board[3].append(orb_string[orb_idx])
        elif orb_idx > 23 and orb_idx <= 29:
            board[4].append(orb_string[orb_idx])
    return board

def check_horizontal(board):
    total = []
    for row in board:
        color_matches = [[], [], [], [], [], []]
        for orb_idx in range(len(row) - 2):
            if row[orb_idx] == row[orb_idx + 1] and row[orb_idx] == row[orb_idx + 2]:
                if row[orb_idx] == 'r':
                    color_matches[0].extend([orb_idx, orb_idx + 1, orb_idx + 2])
                elif row[orb_idx] == 'g':
                    color_matches[1].extend([orb_idx, orb_idx + 1, orb_idx + 2])
                elif row[orb_idx] == 'b':
                    color_matches[2].extend([orb_idx, orb_idx + 1, orb_idx + 2])
                elif row[orb_idx] == 'l':
                    color_matches[3].extend([orb_idx, orb_idx + 1, orb_idx + 2])
                elif row[orb_idx] == 'd':
                    color_matches[4].extend([orb_idx, orb_idx + 1, orb_idx + 2])
                elif row[orb_idx] == 'h':
                    color_matches[5].extend([orb_idx, orb_idx + 1, orb_idx + 2])
        for color_match_idx in range(len(color_matches)):
            color_matches[color_match_idx] = list(dict.fromkeys(color_matches[color_match_idx]))
        total.append(color_matches)
    return total

def check_h_colors(matches):
    r_match= []
    g_match = []
    b_match = []
    l_match = []
    d_match = []
    h_match = []

    for row_idx in range(len(matches)):
        for col_idx in range(len(matches[row_idx])):
            if col_idx == 0:
                r_match.append(matches[row_idx][col_idx])
            elif col_idx == 1:
                g_match.append(matches[row_idx][col_idx])
            elif col_idx == 2:
                b_match.append(matches[row_idx][col_idx])
            elif col_idx == 3:
                l_match.append(matches[row_idx][col_idx])
            elif col_idx == 4:
                d_match.append(matches[row_idx][col_idx])
            elif col_idx == 5:
                h_match.append(matches[row_idx][col_idx])
    # write a doc about timeline


def check_attach(col_matches):

def check_vertical(board):
    pass

def analyze(matches):
    print('Analysis:')
    for row_idx in range(len(matches)):
        empty = True
        match_dic = {}
        for colors_idx in range(len(matches[row_idx])):
            if len(matches[row_idx][colors_idx]) != 0:
                empty = False
                if colors_idx == 0:
                    color = 'Red'
                elif colors_idx == 1:
                    color = 'Green'
                elif colors_idx == 2:
                    color = 'Blue'
                elif colors_idx == 3:
                    color = 'Light'
                elif colors_idx == 4:
                    color = 'Dark'
                elif colors_idx == 5:
                    color = 'Heart'
                match_dic[color] = matches[row_idx][colors_idx]
        if empty:
            print(f'Row {row_idx + 1}: No matches.')
        else:
            data = ''
            for key in match_dic:
                data += f'{key}:  {match_dic[key]} '
            print(f'Row {row_idx + 1}: ' + data)



def main():
    my = ''
    if my == '':
        new_board = start_board()
    else:
        new_board = two_dimension(my.lower())
    gui_board(new_board)

    h_matches = check_horizontal(new_board)
    print(h_matches)
    analyze(h_matches)

main()