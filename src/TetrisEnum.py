from enum import Enum

class BlockShape(Enum):
    Space = 0
    Garbage = 1 # 방해줄
    
    # T-Spin Corner (for 3-corner Rule)
    T_FRONT_CORNER = 8
    T_BACK_CORNER = 9
    
    # 움직이는 블럭
    Liquid = 10
    I = 11 # Liquid 생략
    O = 12
    T = 13
    J = 14
    L = 15
    S = 16
    Z = 17
    
    # 고정된 블럭
    Solid = 20
    Solid_I = 21
    Solid_O = 22
    Solid_T = 23
    Solid_J = 24
    Solid_L = 25
    Solid_S = 26
    Solid_Z = 27
    
    # Ghost
    Ghost = 30,
    
    
class Direction(Enum):
    UP = 1,
    DOWN = 2,
    LEFT = 3,
    RIGHT = 4

class AICondition(Enum):
    PLACING = 0,
    DONE = 1,
    NEED_RELOAD = 2,

class Action(Enum):
    MOVE = 0,
    ROTATE = 1,
    SRS_LAST_OFFSET_ROTATE = 2

class AttackStyle(Enum):
    T_SPIN_MINI = 0,
    T_SPIN = 1,
    T_SPIN_MINI_SINGLE = 2,
    T_SPIN_MINI_DOUBLE = 3,
    T_SPIN_SINGLE = 4,
    T_SPIN_DOUBLE = 5,
    T_SPIN_TRIPLE = 6,
    QUAD = 7,
    TRIPLE = 8,
    DOUBLE = 9,
    SINGLE = 10,
    
    
