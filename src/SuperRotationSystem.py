from TetrisEnum import BlockShape

def WallKickData(testNum, rotateState, crntBlockShape:BlockShape, clockWise = True) -> tuple:
        if crntBlockShape in [BlockShape.J, BlockShape.L, BlockShape.S, BlockShape.T, BlockShape.Z]:
            if clockWise:
                if rotateState == 0:
                    testPosition = {1:(0,0), 2:(-1, 0), 3:(-1, 1), 4:(0, -2), 5:(-1, -2)}
                    return testPosition.get(testNum)
                elif rotateState == 1:
                    testPosition = {1:(0,0), 2:(1, 0), 3:(1, -1), 4:(0, 2), 5:(1, 2)}
                    return testPosition.get(testNum)
                elif rotateState == 2:
                    testPosition = {1:(0,0), 2:(1, 0), 3:(1, 1), 4:(0, -2), 5:(1, -2)}
                    return testPosition.get(testNum)   
                elif rotateState == 3:
                    testPosition = {1:(0,0), 2:(-1, 0), 3:(-1, -1), 4:(0, 2), 5:(-1, 2)}
                    return testPosition.get(testNum)
                
            else: # clockWise == False
                if rotateState == 0:
                    testPosition = {1:(0,0), 2:(1, 0), 3:(1, 1), 4:(0, -2), 5:(1, -2)}
                    return testPosition.get(testNum)
                elif rotateState == 1:
                    testPosition = {1:(0,0), 2:(1, 0), 3:(1, -1), 4:(0, 2), 5:(1, 2)}
                    return testPosition.get(testNum)
                elif rotateState == 2:
                    testPosition = {1:(0,0), 2:(-1, 0), 3:(-1, 1), 4:(0, -2), 5:(-1, -2)}
                    return testPosition.get(testNum)   
                elif rotateState == 3:
                    testPosition = {1:(0,0), 2:(-1, 0), 3:(-1, -1), 4:(0, 2), 5:(-1, 2)}
                    return testPosition.get(testNum)
                
        elif crntBlockShape == BlockShape.I:
            if clockWise:
                if rotateState == 0:
                    testPosition = {1:(0,0), 2:(-2, 0), 3:(1, 0), 4:(-2, -1), 5:(1, 2)}
                    return testPosition.get(testNum)
                elif rotateState == 1:
                    testPosition = {1:(0,0), 2:(-1, 0), 3:(2, 0), 4:(-1, 2), 5:(2, -1)}
                    return testPosition.get(testNum)
                elif rotateState == 2:
                    testPosition = {1:(0,0), 2:(2, 0), 3:(-1, 0), 4:(2, 1), 5:(-1, -2)}
                    return testPosition.get(testNum)
                elif rotateState == 3:
                    testPosition = {1:(0,0), 2:(1, 0), 3:(-2, 0), 4:(1, -2), 5:(-2, 1)}
                    return testPosition.get(testNum)

            else:
                if rotateState == 0:
                    testPosition = {1:(0,0), 2:(-1, 0), 3:(2, 0), 4:(-1, 2), 5:(2, -1)}
                    return testPosition.get(testNum)
                elif rotateState == 1:
                    testPosition = {1:(0,0), 2:(2, 0), 3:(-1, 0), 4:(2, 1), 5:(-1, -2)}
                    return testPosition.get(testNum)
                elif rotateState == 2:
                    testPosition = {1:(0,0), 2:(1, 0), 3:(-2, 0), 4:(1, -2), 5:(-2, 1)}
                    return testPosition.get(testNum)
                elif rotateState == 3:
                    testPosition = {1:(0,0), 2:(-2, 0), 3:(1, 0), 4:(-2, -1), 5:(1, 2)}
                    return testPosition.get(testNum)
        else:
            return (0, 0)
