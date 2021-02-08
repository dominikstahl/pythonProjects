from tictactoe_functions import *

again = True
while again:
    while True:
        mode = input("Ein (1) oder zwei (2) Spieler? ")
        if mode == "1":
            while True:
                player_choice = input(
                    "Waehlst du Kreuze (1) oder Kreise (2)? (Kreuz beginnt) "
                )
                if player_choice == "1":
                    npc_plays = 2
                    break
                elif player_choice == "2":
                    npc_plays = 1
                    break
            break
        elif mode == "2":
            npc_plays = 0
            break

    player_data = (set(), set())
    while len(player_data[0] | player_data[1]) < 9:
        if npc_plays == 1:
            player_data[0].add(do_best_turn(player_data, 1))
        else:
            player_data[0].add(do_human_turn(player_data, 1, npc_plays))
        if check_victory(player_data):
            break
        if len(player_data[0] | player_data[1]) >= 9:
            break
        if npc_plays == 2:
            player_data[1].add(do_best_turn(player_data, 2))
        else:
            player_data[1].add(do_human_turn(player_data, 2, npc_plays))
        if check_victory(player_data):
            break
    build_board(player_data)
    if check_victory(player_data) == 0:
        print("Unentschieden.")
    elif check_victory(player_data) == 1:
        if npc_plays == 0:
            print("Spieler 1 gewinnt.")
        elif npc_plays == 1:
            print("Du verlierst.")
        else:
            print("Du gewinnst.")
    else:
        if npc_plays == 0:
            print("Spieler 2 gewinnt.")
        elif npc_plays == 1:
            print("Du gewinnst.")
        else:
            print("Du verlierst.")
    while True:
        again = input("Nochmal? (J/N) ")
        if again == "J":
            again = True
            break
        elif again == "N":
            again = False
            break
