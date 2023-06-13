import PyGameGUI as GUI
from Player import AIPlayer, TetrisPlayer


def gameStart(playerTuple):
    GUI.startMainLoop(playerTuple) # playerTuple를 GUI에게도 넘겨준다.

if __name__ == "__main__":
    GUI.initScreen()
    player1 = TetrisPlayer(1) 
    player2 = AIPlayer(2)
    

    playerTuple = (player1, player2)
    gameStart(playerTuple) # playerTuple를 넘겨주어 이를 통해 작동하도록 한다.
