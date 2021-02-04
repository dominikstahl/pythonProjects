import random

def build_board(player_data,show_numbers=False):
    if show_numbers:
        board = ['1','2','3','4','5','6','7','8','9']
    else:
        board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    for i in range(9):
        if i in player_data[0]:
            board[i] = 'X'
        elif i in player_data[1]:
            board[i] = 'O'
    for j in range(3):
        print("+---+---+---+")
        print("| "+board[3*j]+" | "+board[3*j+1]+" | "+board[3*j+2]+" |")
    print("+---+---+---+")

def do_best_turn(player_data,whose_turn):
    if len(player_data[0]|player_data[1])==0:
        return random.choice(range(9))
    if whose_turn==1:
        current_winner = -2
    else:
        current_winner = 2
    best_choices = set()
    for turn in ((set(range(9))-(player_data[0]|player_data[1]))):
        scenario = (player_data[0].copy(),player_data[1].copy())
        scenario[whose_turn-1].add(turn)
        next_whose_turn = (not(whose_turn-1))+1
        winner = who_wins(scenario,next_whose_turn)
        if winner==2:
            winner = -1
        if winner==current_winner:
            best_choices.add(turn)
        elif ( winner>current_winner and whose_turn==1 ) or ( winner<current_winner and whose_turn==2 ):
            best_choices = set()
            best_choices.add(turn)
            current_winner = winner
    return random.choice(tuple(best_choices))

def who_wins(player_data,whose_turn):
    if check_victory(player_data):
        return check_victory(player_data)
    elif len(player_data[0]|player_data[1])==9:
        return 0
    next_player_data = (player_data[0].copy(),player_data[1].copy())
    next_player_data[whose_turn-1].add(do_best_turn(next_player_data,whose_turn))
    next_whose_turn = (not(whose_turn-1))+1
    return who_wins(next_player_data,next_whose_turn)

def do_human_turn(player_data,whose_turn,npc_plays):
    if npc_plays:
        string = "Dein Zug: "
    else:
        if whose_turn==1:
            string = "Spieler 1, dein Zug: "
        else:
            string = "Spieler 2, dein Zug: "
    while True:
        build_board(player_data,True)
        turn = input(string)
        if turn in ['1','2','3','4','5','6','7','8','9']:
            if int(turn)-1 in (set(range(9))-(player_data[0]|player_data[1])):
                return int(turn)-1

def check_victory(player_data):
    for i in range(3):
        for j in [0,1]:
            if 3*i+0 in player_data[j] and 3*i+1 in player_data[j] and 3*i+2 in player_data[j]:
                return j+1
            elif i in player_data[j] and i+3 in player_data[j] and i+6in player_data[j]:
                return j+1
            elif 0 in player_data[j] and 4 in player_data[j] and 8 in player_data[j]:
                return j+1
            elif 2 in player_data[j] and 4 in player_data[j] and 6 in player_data[j]:
                return j+1
    return 0
