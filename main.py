from get_user_input import get_user_input
from update_board import update_board
from view_board import view_board
from set_up_game import set_up_game
from check import check

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'\t\t\t\t\t {name}')  # Press Ctrl+F8 to toggle the breakpoint.



if __name__ == '__main__':
    print_hi('***** Welcome User, Tic Tac Toe *****')
    board = [[' ',' ',' ' ],[' ',' ',' ' ],[' ',' ',' ' ]]
    player_1,player_2 = set_up_game()
    view_board(board=board)
    print("\t\t\t PLAYER 1 starts the game !")

    check_it = True
    # while the check is true
    iteration = 0

    while check_it:
        if iteration%2==0:
            position = get_user_input(board=board)
            update_board(position=position , board=board ,player=player_1)
            temp,result = check(board,p1=player_1,p2=player_2)
            iteration+=1
            if temp=="0":
                check_it=False
        else:
            position = get_user_input(board=board)
            update_board(position=position, board=board, player=player_2)
            temp,result = check(board,p1=player_1,p2=player_2)
            iteration += 1
            if temp == "0":
                check_it = False

    print(f"RESULT : {result}")



