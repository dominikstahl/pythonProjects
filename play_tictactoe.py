from tictactoe_functions import *

again = True
while again:
    while True:
        mode = input("Ein (1) oder zwei (2) Spieler? ")
        if mode=='1':
            while True:
                playerChoice = input("Waehlst du Kreuze (1) oder Kreise (2)? (Kreuz beginnt) ")
                if playerChoice=='1':
                    npcPlays = 2
                    break
                elif playerChoice=='2':
                    npcPlays = 1
                    break
            break
        elif mode=='2':
            npcPlays = 0
            break

    playerData = (set(),set())
    while len(playerData[0]|playerData[1])<9:
        if npcPlays==1:
            playerData[0].add(doBestTurn(playerData,1))
        else:
            playerData[0].add(doHumanTurn(playerData,1,npcPlays))
        if checkVictory(playerData):
            break
        if len(playerData[0]|playerData[1])>=9:
            break
        if npcPlays==2:
            playerData[1].add(doBestTurn(playerData,2))
        else:
            playerData[1].add(doHumanTurn(playerData,2,npcPlays))
        if checkVictory(playerData):
            break
    buildBoard(playerData)
    if checkVictory(playerData)==0:
        print("Unentschieden.")
    elif checkVictory(playerData)==1:
        if npcPlays==0:
            print("Spieler 1 gewinnt.")
        elif npcPlays==1:
            print("Du verlierst.")
        else:
            print("Du gewinnst.")
    else:
        if npcPlays==0:
            print("Spieler 2 gewinnt.")
        elif npcPlays==1:
            print("Du gewinnst.")
        else:
            print("Du verlierst.")
    while True:
        again = input("Nochmal? (J/N) ")
        if again=='J':
            again = True
            break
        elif again=='N':
            again = False
            break
