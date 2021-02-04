import random

def buildBoard(playerData,showNumbers=False):
    if showNumbers:
        board = ['1','2','3','4','5','6','7','8','9']
    else:
        board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    for i in range(9):
        if i in playerData[0]:
            board[i] = 'X'
        elif i in playerData[1]:
            board[i] = 'O'
    for j in range(3):
        print("+---+---+---+")
        print("| "+board[3*j]+" | "+board[3*j+1]+" | "+board[3*j+2]+" |")
    print("+---+---+---+")

def doBestTurn(playerData,whoseTurn):
    if len(playerData[0]|playerData[1])==0:
        return random.choice(range(9))
    if whoseTurn==1:
        currentWinner = -2
    else:
        currentWinner = 2
    bestChoices = set()
    for turn in ((set(range(9))-(playerData[0]|playerData[1]))):
        scenario = (playerData[0].copy(),playerData[1].copy())
        scenario[whoseTurn-1].add(turn)
        nextWhoseTurn = (not(whoseTurn-1))+1
        winner = whoWins(scenario,nextWhoseTurn)
        if winner==2:
            winner = -1
        if winner==currentWinner:
            bestChoices.add(turn)
        elif ( winner>currentWinner and whoseTurn==1 ) or ( winner<currentWinner and whoseTurn==2 ):
            bestChoices = set()
            bestChoices.add(turn)
            currentWinner = winner
    return random.choice(tuple(bestChoices))

def whoWins(playerData,whoseTurn):
    if checkVictory(playerData):
        return checkVictory(playerData)
    elif len(playerData[0]|playerData[1])==9:
        return 0
    nextPlayerData = (playerData[0].copy(),playerData[1].copy())
    nextPlayerData[whoseTurn-1].add(doBestTurn(nextPlayerData,whoseTurn))
    nextWhoseTurn = (not(whoseTurn-1))+1
    return whoWins(nextPlayerData,nextWhoseTurn)

def doHumanTurn(playerData,whoseTurn,npcPlays):
    if npcPlays:
        string = "Dein Zug: "
    else:
        if whoseTurn==1:
            string = "Spieler 1, dein Zug: "
        else:
            string = "Spieler 2, dein Zug: "
    while True:
        buildBoard(playerData,True)
        turn = input(string)
        if turn in ['1','2','3','4','5','6','7','8','9']:
            if int(turn)-1 in (set(range(9))-(playerData[0]|playerData[1])):
                return int(turn)-1

def checkVictory(playerData):
    for i in range(3):
        for j in [0,1]:
            if 3*i+0 in playerData[j] and 3*i+1 in playerData[j] and 3*i+2 in playerData[j]:
                return j+1
            elif i in playerData[j] and i+3 in playerData[j] and i+6in playerData[j]:
                return j+1
            elif 0 in playerData[j] and 4 in playerData[j] and 8 in playerData[j]:
                return j+1
            elif 2 in playerData[j] and 4 in playerData[j] and 6 in playerData[j]:
                return j+1
    return 0
