# Tetromino -> I, O, T, J, L, S, Z
import random
from TetrisEnum import BlockShape
        
ITetromino = [
    [   
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0]    
    ], 
    [   
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0]
    ], 
    [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0]
    ], 
    [
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0]
    ]
]
OTetromino = [
    [
        [0, 2, 2, 0],
        [0, 2, 2, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ], 
    [
        [0, 2, 2, 0],
        [0, 2, 2, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ], 
    [
        [0, 2, 2, 0],
        [0, 2, 2, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ], 
    [
        [0, 2, 2, 0],
        [0, 2, 2, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
]
TTetromino = [
    [
        [8, 3, 8, 0],
        [3, 3, 3, 0],
        [9, 0, 9, 0],
        [0, 0, 0, 0]
    ], 
    [
        [9, 3, 8, 0],
        [0, 3, 3, 0],
        [9, 3, 8, 0],
        [0, 0, 0, 0]
    ], 
    [
        [9, 0, 9, 0],
        [3, 3, 3, 0],
        [8, 3, 8, 0],
        [0, 0, 0, 0]
    ], 
    [
        [8, 3, 9, 0],
        [3, 3, 0, 0],
        [8, 3, 9, 0],
        [0, 0, 0, 0]
    ]
]
JTetromino = [
    [
        [4, 0, 0, 0],
        [4, 4, 4, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ], 
    [
        [0, 4, 4, 0],
        [0, 4, 0, 0],
        [0, 4, 0, 0],
        [0, 0, 0, 0]
    ], 
    [
        [0, 0, 0, 0],
        [4, 4, 4, 0],
        [0, 0, 4, 0],
        [0, 0, 0, 0]
    ], 
    [
        [0, 4, 0, 0],
        [0, 4, 0, 0],
        [4, 4, 0, 0],
        [0, 0, 0, 0]
    ]
]
LTetromino = [
    [
        [0, 0, 5, 0],
        [5, 5, 5, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ], 
    [
        [0, 5, 0, 0],
        [0, 5, 0, 0],
        [0, 5, 5, 0],
        [0, 0, 0, 0]
    ], 
    [
        [0, 0, 0, 0],
        [5, 5, 5, 0],
        [5, 0, 0, 0],
        [0, 0, 0, 0]
    ], 
    [
        [5, 5, 0, 0],
        [0, 5, 0, 0],
        [0, 5, 0, 0],
        [0, 0, 0, 0]
    ]
]
STetromino = [
    [
        [0, 6, 6, 0],
        [6, 6, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ], 
    [
        [0, 6, 0, 0],
        [0, 6, 6, 0],
        [0, 0, 6, 0],
        [0, 0, 0, 0]
    ], 
    [
        [0, 0, 0, 0],
        [0, 6, 6, 0],
        [6, 6, 0, 0],
        [0, 0, 0, 0]
    ], 
    [
        [6, 0, 0, 0],
        [6, 6, 0, 0],
        [0, 6, 0, 0],
        [0, 0, 0, 0]
    ]
]
ZTetromino = [
    [
        [7, 7, 0, 0],
        [0, 7, 7, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ], 
    [
        [0, 0, 7, 0],
        [0, 7, 7, 0],
        [0, 7, 0, 0],
        [0, 0, 0, 0]
    ], 
    [
        [0, 0, 0, 0],
        [7, 7, 0, 0],
        [0, 7, 7, 0],
        [0, 0, 0, 0]
    ], 
    [
        [0, 7, 0, 0],
        [7, 7, 0, 0],
        [7, 0, 0, 0],
        [0, 0, 0, 0]
    ]
]

def blockFetch(mino: BlockShape, rot: int = 0):
    intBlockArray = [[0, 0, 0, 0], 
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]
    BlockArray = [[BlockShape.Space, BlockShape.Space, BlockShape.Space, BlockShape.Space],
                  [BlockShape.Space, BlockShape.Space, BlockShape.Space, BlockShape.Space],
                  [BlockShape.Space, BlockShape.Space, BlockShape.Space, BlockShape.Space],
                  [BlockShape.Space, BlockShape.Space, BlockShape.Space, BlockShape.Space]]
    if mino == BlockShape.I:
        intBlockArray = ITetromino[rot]
    elif mino == BlockShape.O:
        intBlockArray = OTetromino[rot]
    elif mino == BlockShape.T:
        intBlockArray = TTetromino[rot]
    elif mino == BlockShape.J:
        intBlockArray = JTetromino[rot]
    elif mino == BlockShape.L:
        intBlockArray = LTetromino[rot]
    elif mino == BlockShape.S:
        intBlockArray = STetromino[rot]
    else:
        intBlockArray = ZTetromino[rot]
    
    for r in range(4):
        for c in range(4):
            if intBlockArray[r][c] == 1:
                BlockArray[r][c] = BlockShape.I
            elif intBlockArray[r][c] == 2:
                BlockArray[r][c] = BlockShape.O
            elif intBlockArray[r][c] == 3:
                BlockArray[r][c] = BlockShape.T
            elif intBlockArray[r][c] == 4:
                BlockArray[r][c] = BlockShape.J
            elif intBlockArray[r][c] == 5:
                BlockArray[r][c] = BlockShape.L
            elif intBlockArray[r][c] == 6:
                BlockArray[r][c] = BlockShape.S
            elif intBlockArray[r][c] == 7:
                BlockArray[r][c] = BlockShape.Z
            elif intBlockArray[r][c] == 8:
                BlockArray[r][c] = BlockShape.T_FRONT_CORNER
            elif intBlockArray[r][c] == 9:
                BlockArray[r][c] = BlockShape.T_BACK_CORNER
    return BlockArray
class Position():
    def __init__(self, ini_r, ini_c):
        self.r = ini_r
        self.c = ini_c
        
class Block():
    
    def __init__(self):
        self.nextBlockList:list[BlockShape] = []
        self.BAG:int = 7 # const
        self.usedBlockCount:int = 0
        self.crntBlockShape:BlockShape
        self.crntBlockArray:list[list[int]]
        self.crntBlockPos = Position(0, 3)
        self.rotationState:int = 0
        self.ghostBlockPos = Position(0, 3)
        self.holdBlockShape:BlockShape = BlockShape.Space
    
    def setNextBlockList(self): # set initial next blocks array
        firstBag, secondBag = [], []
        for T in range(0, 2):
            blockShapeDic = {1:BlockShape.I, 2:BlockShape.O, 3:BlockShape.T, 4:BlockShape.J, 5:BlockShape.L, 6:BlockShape.S, 7:BlockShape.Z}
            for _ in range(self.BAG):
                randNum = random.randint(1, self.BAG)
                randBlockShape = blockShapeDic.get(randNum, None) # random BlockShape
                if T == 1:
                    while(randBlockShape in firstBag):
                        randNum = random.randint(1, self.BAG)
                        randBlockShape = blockShapeDic.get(randNum, None)
                    firstBag.append(randBlockShape)
                else:
                    while(randBlockShape in secondBag):
                        randNum = random.randint(1, self.BAG)
                        randBlockShape = blockShapeDic.get(randNum, None)
                    secondBag.append(randBlockShape)
        for i in firstBag:
            self.nextBlockList.append(i)
        for i in secondBag:
            self.nextBlockList.append(i)

    def updateNextBlockList(self): 
        blockShapeDic = {1:BlockShape.I, 2:BlockShape.O, 3:BlockShape.T, 4:BlockShape.J, 5:BlockShape.L, 6:BlockShape.S, 7:BlockShape.Z}
        secondBag = []
        for i in range(self.BAG):
            self.nextBlockList[i] = self.nextBlockList[i + self.BAG]
        

        for _ in range(self.BAG):
            randNum = random.randint(1, self.BAG)
            randBlockShape = blockShapeDic.get(randNum, None) # random BlockShape
            while(randBlockShape in secondBag):
                randNum = random.randint(1, self.BAG)
                randBlockShape = blockShapeDic.get(randNum, None)
            secondBag.append(randBlockShape)
        
        for i in range(self.BAG):
            self.nextBlockList[i + self.BAG] = secondBag[i]


    def setBlock(self):
        self.crntBlockShape = self.nextBlockList[self.usedBlockCount % self.BAG] 
        self.crntBlockArray = blockFetch(self.crntBlockShape, self.rotationState)
    
    
    def initcrntBlockPos(self):
        self.crntBlockPos = Position(0, 3)
        
    def upload(self, mainTable):
        for r in range(4):
            for c in range(4):
                if self.crntBlockArray[r][c] not in [BlockShape.Space, BlockShape.T_BACK_CORNER, BlockShape.T_FRONT_CORNER]:
                    if mainTable[self.crntBlockPos.r + r][self.crntBlockPos.c + c] != BlockShape.Space:
                        return False
        
        for r in range(4):
            for c in range(4):
                if self.crntBlockArray[r][c] not in [BlockShape.Space, BlockShape.T_BACK_CORNER, BlockShape.T_FRONT_CORNER]:
                    mainTable[self.crntBlockPos.r + r][self.crntBlockPos.c + c] = self.crntBlockArray[r][c]
        return True
    
    def setNextBlock(self, mainTable):
        self.usedBlockCount += 1
        if self.usedBlockCount % self.BAG == 0:
            self.updateNextBlockList()
        self.rotationState = 0
        self.crntBlockPos = Position(0, 3)
        self.setBlock()
        return self.upload(mainTable)
        
