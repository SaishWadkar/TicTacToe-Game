from view_board import view_board

def update_board(position,board,player):
    
    # board[positionition] = player
    if position == 1:
        #print("In position 1")
        board[0][0] = player
    elif position == 2:
        board[0][1] = player
    elif position == 3:
        board[0][2] = player

    elif position == 4:
        board[1][0] = player
    elif position == 5:
        board[1][1] = player
    elif position == 6:
        board[1][2] = player

    elif position == 7:
        board[2][0] = player
    elif position == 8:
        board[2][1] = player
    elif position == 9:
        board[2][2] = player

    print("BOARD UPDATED")
    view_board(board=board)
    return True




