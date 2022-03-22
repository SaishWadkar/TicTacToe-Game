
def is_position_empty(pos,board):
    if pos <= 3:
        if pos == 1 and board[0][0] == ' ':
            return True
        elif pos == 2 and board[0][1] == ' ':
            return True
        elif pos == 3 and board[0][2] == ' ':
            return True

    elif pos > 3 and pos <= 6:
        if pos == 4 and board[1][0] == ' ':
            return True
        elif pos == 5 and board[1][1] == ' ':
            return True
        elif pos == 6 and board[1][2] == ' ':
            return True

    elif pos > 6 and pos <= 9:
        if pos == 7 and board[2][0] == ' ':
            return True
        elif pos == 8 and board[2][1] == ' ':
            return True
        elif pos == 9 and board[2][2] == ' ':
            return True
