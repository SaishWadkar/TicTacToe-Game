
def set_up_game():
    player_1 = None
    player_2 = None
    while player_1 !='X' or player_1!='O':
        player_1 = input("Player 1 , choose your character : (X or O) ->\t")
        if player_1=='X':
            player_2 = 'O'
            break
        elif player_1=='O':
            player_2 = 'X'
            break

    return player_1,player_2

