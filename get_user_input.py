from is_position_empty import is_position_empty


def get_user_input(board):
    position = None
    valid_values = range(1,10) # 1-9 int
    while position not in valid_values:
        position = input("Enter the position (1-9) : ")
        if position.isdigit():
            pos = int(position)
            if pos in valid_values:
                if is_position_empty(pos=pos,board=board):
                    break

    return int(position)

