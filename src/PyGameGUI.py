import pygame
import sys
import time
from Player import Player, TetrisPlayer, AIPlayer
from TetrisEnum import BlockShape, Direction, AICondition

backgroundColor = (153, 153, 153)

def initScreen():
    pygame.init()

    # title
    pygame.display.set_caption("Tetris")

    # screen
    global screen 
    global screenSize
    screenSize = (1280, 720)
    screen = pygame.display.set_mode(screenSize)
    
    drawBackground()

class KeyTimer:
    def __init__(self, key):
        self.key = key
        self.startTime = 0
        self.endTime = 0
        self.keyDownTime = 0
        
    def TimerStart(self):
        self.startTime = time.time()
        
    def TimerStop(self):
        self.endTime = time.time()
        
    def calcKeyDownTime(self):
        self.keyDownTime = self.endTime - self.startTime
        
    def TimerReset(self):
        self.startTime = 0
        self.endTime = 0
        self.keyDownTime = 0
        

def startMainLoop(playerTuple:tuple[TetrisPlayer, AIPlayer]):
    fps = pygame.time.Clock()
    
    tetrisPlayer:TetrisPlayer = playerTuple[0]
    reloadScreen(tetrisPlayer)
    aiPlayer:AIPlayer = playerTuple[1]
    
    keyTimerList:list[KeyTimer] = []
    
    running = True
    tetrisPlayer.timerStart()
    aiPlayer.timerStart()
    aiPlayer.startAutoPlace()
    
    # Main Loop
    while running:
        fps.tick(60)
        
        # 테트리스 플레이어로 계산
        totalGameTime = tetrisPlayer.getTime()
        showGameTime(totalGameTime)
        
        if aiPlayer.condition == AICondition.NEED_RELOAD:
            reloadScreen(aiPlayer)
            if aiPlayer.damage != 0:
                tetrisPlayer.attacked(aiPlayer.damage)
        
            
            aiPlayer.condition = AICondition.DONE
        if tetrisPlayer.doNeedReload == True:
            reloadScreen(tetrisPlayer)
            tetrisPlayer.doNeedReload = False
        
        for timer in keyTimerList:
            if timer.startTime != 0:
                timer.TimerStop()
                timer.calcKeyDownTime()
                if(timer.keyDownTime >= tetrisPlayer.DAS):
                    if timer.key == pygame.K_LEFT:
                        tetrisPlayer.move(Direction.LEFT, True)
                    elif timer.key == pygame.K_RIGHT:
                        tetrisPlayer.move(Direction.RIGHT, True)
                    elif timer.key == pygame.K_DOWN:
                        tetrisPlayer.move(Direction.DOWN, True)
        
                    tetrisPlayer.setGhostBlock()
                    if tetrisPlayer.doNeedReload:
                        reloadScreen(tetrisPlayer)
                        tetrisPlayer.doNeedReload = False        
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if tetrisPlayer.isGameOver == False and event.type == pygame.KEYDOWN:
                # 이동 관련 키 여부 검사
                if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    keyTimer = KeyTimer(event.key)
                    if(event.key in [pygame.K_RIGHT, pygame.K_LEFT]):
                        for timer in keyTimerList:
                            if(timer.key in [pygame.K_LEFT, pygame.K_RIGHT]):
                                keyTimerList.remove(timer)
                    keyTimerList.append(keyTimer)
                    keyTimer.TimerStart()
                    
                    if event.key == pygame.K_UP:
                        reloadScreen(tetrisPlayer)
                        reloadScreen(aiPlayer)
                    elif event.key == pygame.K_DOWN:
                        tetrisPlayer.move(Direction.DOWN, True)
                    elif event.key == pygame.K_LEFT:
                        tetrisPlayer.move(Direction.LEFT)
                    elif event.key == pygame.K_RIGHT:
                        tetrisPlayer.move(Direction.RIGHT)
                        
                    tetrisPlayer.setGhostBlock()
                    keyDownStartTime = time.time()
                    
                elif event.key == pygame.K_SPACE:
                    attack = tetrisPlayer.hardDrop()
                    if attack != 0:
                        aiPlayer.attacked(tetrisPlayer.damage)
                        aiPlayer.condition = AICondition.NEED_RELOAD
                    
                elif event.key == pygame.K_s:
                    tetrisPlayer.rotation(False)
                    
                elif event.key == pygame.K_d:
                    tetrisPlayer.rotation(True)
                    
                elif event.key == pygame.K_ESCAPE:
                    pygame.display.quit() 
                elif event.key == pygame.K_a:
                    tetrisPlayer.hold()
                    
                elif event.key == pygame.K_p:
                    aiPlayer.placeBlockInterval = 99999
                    aiPlayer.placeBlock()
                    print(aiPlayer.costList)
                    
                elif event.key == pygame.K_o:
                    # tetrisPlayer.TcalcCost()
                    totalGameTime = tetrisPlayer.getTime()
                    showGameTime(totalGameTime)
                    
                    
                elif event.key == pygame.K_i:
                    for r in range(20):
                        for c in range(10):
                            print(tetrisPlayer.mainTable[r][c], " ")
                        print()
                if tetrisPlayer.doNeedReload == True:
                    reloadScreen(tetrisPlayer)
                    tetrisPlayer.doNeedReload = False
                    
            if tetrisPlayer.isGameOver == False and event.type == pygame.KEYUP:
                for timer in keyTimerList:
                    if(timer.key == event.key):
                        keyTimerList.remove(timer)
    return

def reloadScreen(player:Player):
    drawGameBoard(player)
    pygame.display.update()
    return

def drawBackground():
    screen.fill((153, 153, 153))
    return

def drawGameBoard(player:Player):
    global blockSize
    blockSize = 30
    gameBoardSize_main = (blockSize * 10, blockSize * 20)
    
    gameBoard_main1 = pygame.Rect((screen.get_size()[0] / 2) - (gameBoardSize_main[0] / 2) - 300, 
                            (screen.get_size()[1] / 2) - (gameBoardSize_main[1] / 2), 
                            gameBoardSize_main[0], 
                            gameBoardSize_main[1])
    gameBoard_main2 = pygame.Rect((screen.get_size()[0] / 2) - (gameBoardSize_main[0] / 2) + 300, 
                            (screen.get_size()[1] / 2) - (gameBoardSize_main[1] / 2), 
                            gameBoardSize_main[0], 
                            gameBoardSize_main[1])
    gameBoard_next1 = pygame.Rect(gameBoard_main1.right + 10, gameBoard_main1.top, blockSize * 4, blockSize * player.visibleNextBlockCount * 3)
    gameBoard_next2 = pygame.Rect(gameBoard_main2.right + 10, gameBoard_main2.top, blockSize * 4, blockSize * player.visibleNextBlockCount * 3)
    
    gameBoard_hold1 = pygame.Rect(gameBoard_main1.left - 10 - blockSize * 4, gameBoard_main1.top, blockSize * 4, blockSize * 4)
    gameBoard_hold2 = pygame.Rect(gameBoard_main2.left - 10 - blockSize * 4, gameBoard_main2.top, blockSize * 4, blockSize * 4)
    
    if player.playerNumber == 1:
        gameBoard_main = gameBoard_main1
        gameBoard_next = gameBoard_next1
        gameBoard_hold = gameBoard_hold1
    else:
        gameBoard_main = gameBoard_main2
        gameBoard_next = gameBoard_next2
        gameBoard_hold = gameBoard_hold2
        
    
    drawMainTable(gameBoard_main, player.mainTable)
    drawNextTable(gameBoard_next, player.nextBlockTable, player.visibleNextBlockCount)
    drawHoldTable(gameBoard_hold, player.holdBlockTable)
    drawGrid(gameBoard_main)    

    return

def drawMainTable(gameBoard:pygame.Rect, mainTable):
    for r in range(20):
        for c in range(10):
            if mainTable[r][c] in [BlockShape.Space, BlockShape.T_FRONT_CORNER, BlockShape.T_BACK_CORNER]:
                color = (153, 153, 153)
            else:
                color = setColor(mainTable[r][c])
            pygame.draw.rect(screen, color, pygame.Rect(gameBoard.x + blockSize * c, gameBoard.y + blockSize * r, blockSize, blockSize))
    return

def drawGrid(gameBoard:pygame.Rect):
    borderThickness = 2
    
    pygame.draw.rect(screen, (0, 0, 0), gameBoard, borderThickness)
    for i in range(1, 20):
        pygame.draw.line(screen, (0, 0, 0), [gameBoard.left, gameBoard.top + (blockSize * i)], [gameBoard.right, gameBoard.top + (blockSize * i)])
    for i in range(1, 10):
        pygame.draw.line(screen, (0, 0, 0), [gameBoard.left + (blockSize * i), gameBoard.top], [gameBoard.left + (blockSize * i), gameBoard.bottom])
    return

def drawHoldTable(gameBoard:pygame.Rect, holdBlockTable):
    for r in range(4):
        for c in range(4):
            if(holdBlockTable[r][c] in [BlockShape.Space, BlockShape.T_FRONT_CORNER, BlockShape.T_BACK_CORNER]):
                color = (153, 153, 153)
            else:
                color = setColor(holdBlockTable[r][c])
            pygame.draw.rect(screen, color, pygame.Rect(gameBoard.x + blockSize * c, gameBoard.y + blockSize * r, blockSize, blockSize))
  
def drawNextTable(gameBoard:pygame.Rect, nextBlockTable, visibleNextBlockCount):
    for r in range(visibleNextBlockCount * 3):
        for c in range(4):
            if(nextBlockTable[r][c] in [BlockShape.Space, BlockShape.T_FRONT_CORNER, BlockShape.T_BACK_CORNER]):
                color = (153, 153, 153)
            else:
                color = setColor(nextBlockTable[r][c])
            pygame.draw.rect(screen, color, pygame.Rect(gameBoard.x + blockSize * c, gameBoard.y + blockSize * r, blockSize, blockSize))

def showGameTime(time:float):
    timeStr = str(time)
    font = pygame.font.SysFont("g마켓산스ttfmedium", 30)

    pygame.draw.rect(screen, backgroundColor, pygame.Rect(130, 10, 90, 20))
    
    timeLetter = font.render(timeStr, True, (255, 255, 255))
    screen.blit(timeLetter, (130, 10))
    pygame.display.flip()


def setColor(blockShape:BlockShape):
    if blockShape == BlockShape.I:
        return (0, 255, 255)
    elif blockShape == BlockShape.J:
        return (0, 0, 255)
    elif blockShape == BlockShape.L:
        return (255, 127, 0)
    elif blockShape == BlockShape.O:
        return (255, 255, 0)
    elif blockShape == BlockShape.S:
        return (0, 255, 0)
    elif blockShape == BlockShape.T:
        return (128, 0, 128)
    elif blockShape == BlockShape.Z:
        return (255, 0, 0)
    elif blockShape == BlockShape.Solid_I:
        return (0, 255, 255)
    elif blockShape == BlockShape.Solid_J:
        return (0, 0, 255)
    elif blockShape == BlockShape.Solid_L:
        return (255, 127, 0)
    elif blockShape == BlockShape.Solid_O:
        return (255, 255, 0)
    elif blockShape == BlockShape.Solid_S:
        return (0, 255, 0)
    elif blockShape == BlockShape.Solid_T:
        return (128, 0, 128)
    elif blockShape == BlockShape.Solid_Z:
        return (255, 0, 0)
    elif blockShape == BlockShape.Ghost:
        return (220, 220, 220)
    elif blockShape == BlockShape.Garbage:
        return (74, 74, 74)
    else:
        return (0, 0, 0)
