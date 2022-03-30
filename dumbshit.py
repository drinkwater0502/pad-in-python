def start_board():
    colors = ['r', 'g', 'b', 'l', 'd', 'h']
    board = [[], [], [], [], []]
    for row in board:
        for i in range(6):
            row.append(random.choice(colors))
    return board

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

    print(r_match)
    print(g_match)
    print(b_match)
    print(l_match)
    print(d_match)
    print(h_match)

    check_h_attach(r_match)
    check_h_attach(g_match)
    check_h_attach(b_match)
    check_h_attach(l_match)
    check_h_attach(d_match)
    check_h_attach(h_match)

def check_h_attach(color_arr):
    groups = []
    groups.append(color_arr[0])
    for i in range(len(color_arr) - 1):
        if len(color_arr[i]) != 0:
            if any(coor in color_arr[i] for coor in color_arr[i + 1]):
                for group_idx in range(len(groups)):
                    if any(grp in color_arr[i] for grp in groups):
                        groups[group_idx].extend(color_arr[i])
                        groups[group_idx].extend(color_arr[i + 1])
            else:
                groups.append(color_arr[i])
    
    for i in range(len(groups)):
        groups[i] = list(dict.fromkeys(groups[i]))

    print(groups)

def check_vertical(board):
    pass