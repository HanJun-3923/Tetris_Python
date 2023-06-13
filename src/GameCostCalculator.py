from TetrisEnum import BlockShape
import copy

class GameCostCalculator:
    heightWeight = 50
    makeHoleWeight = [10, 20, 30, 40, 50]
    clearLineWeight = [0, -10, -20, -30, -50]
    
    """
    블럭의 높이
    구멍을 만드는가
    블럭을 놓았을 때 지워지는 라인의 수
    인접한 솔리드블럭 또는 벽블럭의 수
    
    
    필요한 블럭을 사용해버렸는가
    이 블럭이 아니라면 대체할 블럭이 있는가

    
    """
    
    def __init__(self, mainTable, crntBlockShape):
        self.mainTable = mainTable
        self.crntBlockShape = crntBlockShape
        self.costList = []
        
        
    def getCostToList(self):
        self.costList.clear()
        self.costList.append(copy.deepcopy(self.heightCost()))
        self.costList.append(copy.deepcopy(self.makeHoleCost()))
        self.costList.append(copy.deepcopy(self.clearLineCost()))
        # self.costList.append(copy.deepcopy(self.()))

    def getCost(self) -> float:
        costSum = 0
        self.getCostToList()
        
        for c in self.costList:
            costSum += c
        return costSum
        
    def heightCost(self) -> float:
        minimumRow = None
        for r in range(20):
            for c in range(10):
                if self.mainTable[r][c] == self.crntBlockShape:
                    if minimumRow == None or r < minimumRow:
                        minimumRow = r
        if minimumRow != None:
            maximumHeight = 20 - minimumRow
            return maximumHeight * self.heightWeight
        else:
            return 0

    def clearLineCost(self) -> float:
        clearLineCount = 0
        
        testRow = []
        for r in range(20):
            for c in range(10):
                if self.mainTable[r][c] == self.crntBlockShape:
                    if r not in testRow:
                        testRow.append(r)
                    
        for r in testRow:
            isFull = True
            for c in range(10):
                if self.mainTable[r][c] == BlockShape.Space:
                    isFull = False
                    break
            if isFull == True:
                clearLineCount += 1
                    
        return self.clearLineWeight[clearLineCount]
    
    def makeHoleCost(self) -> float:
        cost = 0
        for r in range(20):
            for c in range(10):
                for deep in range(1, 6):
                    if self.mainTable[r][c] == self.crntBlockShape:
                        if r < 20 - deep and self.mainTable[r + deep][c] in [BlockShape.Space, BlockShape.Ghost]:
                            cost += self.makeHoleWeight[deep - 1]
                        elif r < 20 - deep and self.mainTable[r + deep][c] == self.crntBlockShape:
                            break
        return cost

    