import Tetromino
import threading
import random
from AttackTable import AttackTable
import copy
from GameCostCalculator import GameCostCalculator
import time
import SuperRotationSystem
from TetrisEnum import BlockShape, Direction, AICondition, Action, AttackStyle
from operator import itemgetter

class Player:
    def __init__(self, playerNumber):
        self.mainTable = [[BlockShape.Space] * 10 for row in range(20)]
        self.visibleNextBlockCount = 5
        self.nextBlockTable = [[BlockShape.Space] * 4 for row in range(3 * self.visibleNextBlockCount)]
        self.playerNumber = playerNumber
        self.block = Tetromino.Block()
        self.holdBlockTable = [[BlockShape.Space] * 4 for row in range(4)]
        self.lastAction = None
        
        self.combo = 0
        self.BackToBack = 0
        
        self.damage = 0
        self.PPS = 0
        self.APM = 0
        
        self.startTime = 0
        self.endTime = 0
        self.totalTime = 0
        
        self.block.setNextBlockList()
        self.block.setBlock()
        self.setNextBlockTable()
        self.block.upload(self.mainTable)
        self.doNeedReload = True
        self.isGameOver = False

    
    def move(self, direction:Direction, Maximum = False, upload = True):
        while(True):
            if(self.canMove(direction)):
                self.lastAction = Action.MOVE
                
                if direction == Direction.DOWN:
                    self.block.crntBlockPos.r += 1
                elif direction == Direction.LEFT:
                    self.block.crntBlockPos.c -= 1
                elif direction == Direction.RIGHT:
                    self.block.crntBlockPos.c += 1
                elif direction == Direction.UP:
                    self.block.crntBlockPos.r -= 1
            else:
                break
            if upload == True:
                self.deleteLiquidData()
                self.block.upload(self.mainTable)
                self.doNeedReload = True
            if(Maximum == False):
                break
        return
    
    def canMove(self, direction:Direction = None):    
        for r in range(4):
            for c in range(4):
                pos_r = self.block.crntBlockPos.r + r
                pos_c = self.block.crntBlockPos.c + c
                if self.block.crntBlockArray[r][c] not in [BlockShape.Space, BlockShape.T_BACK_CORNER, BlockShape.T_FRONT_CORNER]:
                    if (0 <= pos_r and pos_r < 20) and (0 <= pos_c and pos_c < 10):
                        testData = None
                        if direction == None:
                            testData = self.mainTable[pos_r][pos_c]
                        elif direction == Direction.DOWN and (0 <= pos_r + 1 and pos_r + 1 < 20):
                            testData = self.mainTable[pos_r + 1][pos_c]
                        elif direction == Direction.LEFT and (0 <= pos_c - 1 and pos_c - 1 < 10):
                            testData = self.mainTable[pos_r][pos_c - 1]
                        elif direction == Direction.RIGHT and (0 <= pos_c + 1 and pos_c + 1 < 10):
                            testData = self.mainTable[pos_r][pos_c + 1]
                        elif direction == Direction.UP and (0 <= pos_r - 1 and pos_r - 1 < 20):
                            testData = self.mainTable[pos_r - 1][pos_c]

                        if testData == None or (testData not in [BlockShape.Space, BlockShape.Ghost, BlockShape.T_BACK_CORNER, BlockShape.T_FRONT_CORNER] and testData != self.block.crntBlockShape):
                            return False
                    else:
                        return False
        return True
    
    def timerStart(self):
        self.startTime = time.time()
    
    def calcTime(self):
        self.endTime = time.time()
        self.totalTime = self.endTime - self.startTime

    def getTime(self):
        self.calcTime()
        roundedTime = round(self.totalTime, 2)
        print(roundedTime)
        return roundedTime

    def deleteLiquidData(self):
        for r in range(20):
            for c in range(10):
                if self.judgeLiquidOrSolid(self.mainTable[r][c]) in [BlockShape.Liquid, BlockShape.Ghost]:
                    self.mainTable[r][c] = BlockShape.Space
        return

    def judgeLiquidOrSolid(self, block:BlockShape) -> BlockShape:
        if block in [BlockShape.I, BlockShape.O, BlockShape.T, BlockShape.L, BlockShape.J, BlockShape.S, BlockShape.Z, BlockShape.T_BACK_CORNER, BlockShape.T_FRONT_CORNER]:
            return BlockShape.Liquid
        elif block in [BlockShape.Solid_I, BlockShape.Solid_O, BlockShape.Solid_T, BlockShape.Solid_L, BlockShape.Solid_J, BlockShape.Solid_S, BlockShape.Solid_Z]:
            return BlockShape.Solid
        elif block == BlockShape.Ghost:
            return BlockShape.Ghost
        elif block == BlockShape.Garbage:
            return BlockShape.Garbage
        else:
            return BlockShape.Space
        
    def solidification(self):
        # find liquid blocks searching mainTable, then replace them to solid blocks
        
        blockShapeDic = {BlockShape.I:BlockShape.Solid_I, BlockShape.O:BlockShape.Solid_O, BlockShape.T:BlockShape.Solid_T, BlockShape.J:BlockShape.Solid_J, BlockShape.L:BlockShape.Solid_L, BlockShape.S:BlockShape.Solid_S, BlockShape.Z:BlockShape.Solid_Z}
        solidBlock = blockShapeDic.get(self.block.crntBlockShape)
            
        for r in range(20):
            for c in range(10):
                if self.judgeLiquidOrSolid(self.mainTable[r][c]) == BlockShape.Liquid and (self.mainTable[r][c] not in [BlockShape.T_BACK_CORNER, BlockShape.T_FRONT_CORNER]):
                    self.mainTable[r][c] = solidBlock
        return
    
    def lineClear(self, OnlyCheck = False):
        clearedLine = 0
        r = 19 
        while r >= 0: # 19 ~ 0
            isFull = True
            if OnlyCheck:
                for c in range(10):
                    if self.judgeLiquidOrSolid(self.mainTable[r][c]) not in [BlockShape.Solid, BlockShape.Garbage, BlockShape.Liquid]:
                        isFull = False
                        break
                if isFull:
                    clearedLine += 1
                r -= 1
            else:
                for c in range(10):
                    if self.judgeLiquidOrSolid(self.mainTable[r][c]) not in [BlockShape.Solid, BlockShape.Garbage]:
                        isFull = False
                        break
                if isFull:
                    clearedLine += 1
                    for r2 in range(r - 1, -1, -1):
                        for c in range(10):
                            self.mainTable[r2 + 1][c] = self.mainTable[r2][c]
                else:
                    r -= 1

        if OnlyCheck:
            return clearedLine
        
    def threeCornerRule(self) -> list:
        '''
        [frontCorner, backCorner]
        '''
        cornerCount = [0, 0]
        for r in range(4):
            for c in range(4):
                if self.block.crntBlockArray[r][c] in [BlockShape.T_FRONT_CORNER, BlockShape.T_BACK_CORNER]:
                    if self.block.crntBlockArray[r][c] == BlockShape.T_FRONT_CORNER:
                        targetIndex = 0
                    else:
                        targetIndex = 1
                    targetPos = Tetromino.Position(r + self.block.crntBlockPos.r, c + self.block.crntBlockPos.c)
                    if (targetPos.r < 0) or (targetPos.r >= 20) or (targetPos.c < 0) or (targetPos.c >= 10):
                        cornerCount[targetIndex] += 1
                    elif self.judgeLiquidOrSolid(self.mainTable[targetPos.r][targetPos.c]) in [BlockShape.Solid, BlockShape.Garbage]:
                        cornerCount[targetIndex] += 1
        return cornerCount
    
    def is_T_Spin(self) -> bool:
        if self.block.crntBlockShape == BlockShape.T:
            if self.lastAction == Action.ROTATE:
                cornerCountList = self.threeCornerRule()
                frontCorner = cornerCountList[0]
                backCorner = cornerCountList[1]
                if frontCorner + backCorner >= 3:
                    if frontCorner == 2 and backCorner == 2:
                        return AttackStyle.T_SPIN
                    elif frontCorner == 1 and backCorner == 2:
                        return AttackStyle.T_SPIN_MINI
                    elif frontCorner == 2 and backCorner == 1:
                        return AttackStyle.T_SPIN
            elif self.lastAction == Action.SRS_LAST_OFFSET_ROTATE:
                return AttackStyle.T_SPIN
        return None

    def setAttackData_getDamage(self):
        '''
        calculate damage, according to combo and BackToBack, and set BackToBack and Combo.
        '''
        t_spin_style = self.is_T_Spin()
        clearedLine = self.lineClear(True)
        
        resultAttackType = None
        if t_spin_style == AttackStyle.T_SPIN:
            if clearedLine == 1:
                resultAttackType = AttackStyle.T_SPIN_SINGLE
            elif clearedLine == 2:
                resultAttackType = AttackStyle.T_SPIN_DOUBLE
            elif clearedLine == 3:
                resultAttackType = AttackStyle.T_SPIN_TRIPLE
        elif t_spin_style == AttackStyle.T_SPIN_MINI:
            if clearedLine == 1:
                resultAttackType = AttackStyle.T_SPIN_MINI_SINGLE
            elif clearedLine == 2:
                resultAttackType = AttackStyle.T_SPIN_MINI_DOUBLE
        elif t_spin_style == None:
            if clearedLine == 1:
                resultAttackType = AttackStyle.SINGLE
            elif clearedLine == 2:
                resultAttackType = AttackStyle.DOUBLE
            elif clearedLine == 3:
                resultAttackType = AttackStyle.TRIPLE
            elif clearedLine == 4:
                resultAttackType = AttackStyle.QUAD
        
        attackTable = AttackTable()
        damage = attackTable.calcDamage(resultAttackType, self.combo, self.BackToBack)

        if t_spin_style in [AttackStyle.T_SPIN, AttackStyle.T_SPIN_MINI] or resultAttackType == AttackStyle.QUAD:
            self.BackToBack += 1
        elif clearedLine > 0:
            self.BackToBack = 0
        
        if clearedLine > 0:
            self.combo += 1
        else:
            self.combo = 0
        
        self.damage = damage
        # print(f"AttackStyle: {resultAttackType}, combo: {self.combo}, damage: {damage}, B2B: {self.BackToBack}")
    
    def setNextBlockTable(self):
        for r in range(self.visibleNextBlockCount * 3):
            for c in range(4):
                self.nextBlockTable[r][c] = BlockShape.Space

        nextBlocks = []
        for i in range(self.visibleNextBlockCount):
            nextBlocks.append(self.block.nextBlockList[self.block.usedBlockCount % self.block.BAG + i + 1])
        
        pos_r = 0
        for block in nextBlocks:
            blockArray = Tetromino.blockFetch(block, 0)
            for r in range(3):
                for c in range(4):
                    self.nextBlockTable[pos_r + r][c] = blockArray[r][c]
            pos_r += 3
    
    def setHoldBlockTable(self):
        for r in range(4):
            for c in range(4):
                self.holdBlockTable[r][c] = BlockShape.Space
        if self.block.holdBlockShape != BlockShape.Space:
            block = Tetromino.blockFetch(self.block.holdBlockShape, 0)
            for r in range(4):
                for c in range(4):
                    self.holdBlockTable[r][c] = block[r][c]
           
    def gameOver(self):
        self.isGameOver = True
        print("Game Over!")

    def attacked(self, damage):
        self.doNeedReload = True
        self.setGarbageLine(damage)
        print(f"attacked! - {damage}")
    
    def setGarbageLine(self, damage):
        if damage == 0:
            return
        garbageTable = [[BlockShape.Space] * 10 for row in range(damage)]
        for r in range(damage):
            randomHole = random.randrange(0, 10)
            for c in range(10):
                if c == randomHole:
                    garbageTable[r][c] = BlockShape.Space
                else:
                    garbageTable[r][c] = BlockShape.Garbage
        for target_r in range(damage, 20):
            for c in range(10):
                self.mainTable[target_r - damage][c] = self.mainTable[target_r][c]
        for r in range(damage):
            for c in range(10):
                self.mainTable[20 - damage + r][c] = garbageTable[r][c]
            
    def calcInfomation(self):
        
        """
        APM: Attack Per Minute
        PPS: Piece Per Second
        """
        pass
        
        
        
           
            
class TetrisPlayer(Player):
    def __init__(self, playerNumber):
        super().__init__(playerNumber)
        self.setGhostBlock()
        self.usedHold:bool = False
        self.DAS = 0.14
        
    def hardDrop(self) -> bool:
        '''
        If there is an garbage line attacking the opponent, the function returns true; otherwise, it returns false.
        '''
        self.doNeedReload = True
        self.move(Direction.DOWN, True)
        
        self.setAttackData_getDamage()
        self.solidification()
        self.lineClear()
        
        
        if not self.block.setNextBlock(self.mainTable):
            self.gameOver()
        self.setNextBlockTable()
        self.setGhostBlock()
        self.usedHold = False
        
        if self.damage != 0:
            return True
        else:
            return False

    def rotation(self, clockWise = True):
        nowPosition = copy.deepcopy(self.block.crntBlockPos)
        nowRotationState = copy.deepcopy(self.block.rotationState)
        for testNum in range(1, 6):
            OffsetPos = SuperRotationSystem.WallKickData(testNum, self.block.rotationState, self.block.crntBlockShape, clockWise)
            self.block.crntBlockPos.c = self.block.crntBlockPos.c + OffsetPos[0]
            self.block.crntBlockPos.r = self.block.crntBlockPos.r - OffsetPos[1]
            if clockWise:
                self.block.rotationState += 1
                if self.block.rotationState >= 4:
                    self.block.rotationState -= 4
            else:
                self.block.rotationState -= 1
                if self.block.rotationState < 0:
                    self.block.rotationState += 4
            self.block.setBlock()
            
            if self.canMove():
                if testNum == 5:
                    self.lastAction = Action.SRS_LAST_OFFSET_ROTATE
                else:
                    self.lastAction = Action.ROTATE
                self.deleteLiquidData()
                self.block.upload(self.mainTable)
                self.doNeedReload = True
                self.setGhostBlock()
                break
            else:
                self.block.rotationState = copy.deepcopy(nowRotationState)
                self.block.crntBlockPos = copy.deepcopy(nowPosition)
    
    def setGhostBlock(self):
        nowPos = copy.deepcopy(self.block.crntBlockPos)
        self.move(Direction.DOWN, True, False)
        ghostPos:Tetromino.Position = copy.deepcopy(self.block.crntBlockPos)
        
        self.block.crntBlockPos = copy.deepcopy(nowPos)
        
        for r in range(4):
            for c in range(4):
                if self.block.crntBlockArray[r][c] not in [BlockShape.Space, BlockShape.T_BACK_CORNER, BlockShape.T_FRONT_CORNER]:
                    if self.mainTable[ghostPos.r + r][ghostPos.c + c] == BlockShape.Space:
                        self.mainTable[ghostPos.r + r][ghostPos.c + c] = BlockShape.Ghost

    def hold(self):
        if self.usedHold:
            return
        else:
            self.usedHold = True

        if self.block.holdBlockShape == BlockShape.Space:
            self.block.holdBlockShape = self.block.crntBlockShape
            self.deleteLiquidData()
            self.block.setNextBlock(self.mainTable)
        else:
            # swap
            temp = self.block.crntBlockShape
            self.block.crntBlockShape = self.block.holdBlockShape
            self.block.holdBlockShape = temp
            self.block.nextBlockList[self.block.usedBlockCount % 7] = self.block.crntBlockShape
            
            self.deleteLiquidData()
            self.block.initcrntBlockPos()
            self.block.rotationState = 0
            self.block.setBlock()
            self.block.upload(self.mainTable)
        
        self.doNeedReload = True
        self.setHoldBlockTable()
        self.setNextBlockTable()
        self.setGhostBlock()
    def TcalcCost(self):
        cal = GameCostCalculator(self.mainTable, self.block.crntBlockShape)
        cost = cal.getCost()
        costList = cal.getCostToList()
        
        print(costList, " += ", cost)
    
class AIPlayer(Player):
    placeBlockInterval = 0.2
    condition = AICondition.DONE
    
    costList = [] # for test
        
    def calcCost(self):
        calculator = GameCostCalculator(self.mainTable, self.block.crntBlockShape)
        
        totalCost = calculator.getCost()
        
        return totalCost
    
    
    
    def setPosition(self, position:Tetromino.Position):
        self.block.crntBlockPos.r = position.r
        self.block.crntBlockPos.c = position.c
        self.deleteLiquidData()
        self.block.upload(self.mainTable)
    
    def placeBlock(self):
        if self.isGameOver:
            return
        # macro function for AI to place current block on the best position
        self.condition = AICondition.PLACING

        cost = []
        if self.block.crntBlockShape == BlockShape.O:
            repeatRange = 1  
        elif self.block.crntBlockShape == BlockShape.T:
            repeatRange = 4
        else:
            repeatRange = 2
        
        
        for rot in range(repeatRange):
            self.block.rotationState = rot
            self.block.setBlock()
            self.block.initcrntBlockPos()
            self.move(Direction.LEFT, True, False)
            self.move(Direction.DOWN, True, False)
            while(True):
                self.deleteLiquidData()
                self.block.upload(self.mainTable)
                cost.append([self.calcCost(), copy.deepcopy(self.block.crntBlockPos), copy.deepcopy(self.block.rotationState), copy.deepcopy(self.costList)])
                self.move(Direction.UP, True, False)
                self.block.upload(self.mainTable)
                if(self.canMove(Direction.RIGHT) == False):
                    break
                self.move(Direction.RIGHT, False, False)
                self.move(Direction.DOWN, True, False)
        
        sortedCost = sorted(cost, key=itemgetter(0))
        self.block.rotationState = sortedCost[0][2]
        self.block.setBlock()
        self.setPosition(sortedCost[0][1])
        
        
        self.costList = sortedCost[0][3]
        
        self.setAttackData_getDamage()
        self.solidification()
        self.lineClear()
        if not self.block.setNextBlock(self.mainTable):
            self.gameOver()
        self.setNextBlockTable()
        
        self.condition = AICondition.NEED_RELOAD
        return
    
    def startAutoPlace(self, placeBlockInterval = placeBlockInterval):
        if self.isGameOver:
            return
        timer = threading.Timer(placeBlockInterval, self.startAutoPlace)
        self.placeBlock()
        timer.start()
    