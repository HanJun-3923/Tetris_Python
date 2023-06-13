from TetrisEnum import AttackStyle

class AttackTable:
    
    def calcDamage(self, attackType:AttackStyle, combo:int, BackToBack:int):
        attackDic = None
        if BackToBack == 0:
            B2B_Level = 0
        elif 1 <= BackToBack and BackToBack <= 2:
            B2B_Level = 1
        elif 3 <= BackToBack and BackToBack <= 7:
            B2B_Level = 2
        elif 8 <= BackToBack and BackToBack <= 23:
            B2B_Level = 3
        else:
            B2B_Level = 4
        
        if attackType == None:
            attackDic = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0, 20:0}
        elif attackType == AttackStyle.SINGLE:
            attackDic = {0:0, 1:0, 2:1, 3:1, 4:1, 5:1, 6:2, 7:2, 8:2, 9:2, 10:2, 11:2, 12:2, 13:2, 14:2, 15:2, 16:3, 17:3, 18:3, 19:3, 20:3}
        elif attackType == AttackStyle.DOUBLE:
            attackDic = {0:1, 1:1, 2:1, 3:1, 4:2, 5:2, 6:2, 7:2, 8:3, 9:3, 10:3, 11:3, 12:4, 13:4, 14:4, 15:4, 16:5, 17:5, 18:5, 19:5, 20:5}
        elif attackType == AttackStyle.TRIPLE:
            attackDic = {0:2, 1:2, 2:3, 3:3, 4:4, 5:4, 6:5, 7:5, 8:6, 9:6, 10:7, 11:7, 12:8, 13:8, 14:9, 15:9, 16:10, 17:10, 18:11, 19:11, 20:12}
        else:
            if B2B_Level == 0:
                if attackType == AttackStyle.QUAD:
                    attackDic = {0:4, 1:5, 2:6, 3:7, 4:8, 5:9, 6:10, 7:11, 8:12, 9:13, 10:14, 11:15, 12:16, 13:17, 14:18, 15:19, 16:20, 17:21, 18:22, 19:23, 20:24}
                elif attackType == AttackStyle.T_SPIN_MINI_SINGLE:
                    attackDic = {0:0, 1:0, 2:1, 3:1, 4:1, 5:1, 6:2, 7:12, 8:2, 9:2, 10:2, 11:2, 12:2, 13:2, 14:2, 15:2, 16:3, 17:3, 18:3, 19:3, 20:3}
                elif attackType == AttackStyle.T_SPIN_SINGLE:
                    attackDic = {0:2, 1:2, 2:3, 3:3, 4:4, 5:4, 6:5, 7:5, 8:6, 9:6, 10:7, 11:7, 12:8, 13:8, 14:9, 15:9, 16:10, 17:10, 18:11, 19:11, 20:12}
                elif attackType == AttackStyle.T_SPIN_MINI_DOUBLE:
                    attackDic = {0:1, 1:1, 2:1, 3:1, 4:2, 5:2, 6:2, 7:2, 8:3, 9:3, 10:3, 11:3, 12:4, 13:4, 14:4, 15:4, 16:5, 17:5, 18:5, 19:5, 20:5}
                elif attackType == AttackStyle.T_SPIN_DOUBLE:
                    attackDic = {0:4, 1:5, 2:6, 3:7, 4:8, 5:9, 6:10, 7:11, 8:12, 9:13, 10:14, 11:15, 12:16, 13:17, 14:18, 15:19, 16:20, 17:21, 18:22, 19:23, 20:24}
                elif attackType == AttackStyle.T_SPIN_TRIPLE:
                    attackDic = {0:6, 1:7, 2:9, 3:10, 4:12, 5:13, 6:15, 7:16, 8:18, 9:19, 10:21, 11:22, 12:24, 13:25, 14:27, 15:28, 16:30, 17:31, 18:33, 19:34, 20:36}
            elif B2B_Level == 1:
                if attackType == AttackStyle.QUAD:
                    attackDic = {0:5, 1:6, 2:7, 3:8, 4:10, 5:11, 6:12, 7:13, 8:15, 9:16, 10:17, 11:18, 12:20, 13:21, 14:22, 15:23, 16:25, 17:26, 18:27, 19:28, 20:30}
                elif attackType == AttackStyle.T_SPIN_MINI_SINGLE:
                    attackDic = {0:1, 1:1, 2:1, 3:1, 4:2, 5:2, 6:2, 7:2, 8:3, 9:3, 10:3, 11:3, 12:4, 13:4, 14:4, 15:4, 16:5, 17:5, 18:5, 19:5, 20:5}
                elif attackType == AttackStyle.T_SPIN_SINGLE:
                    attackDic = {0:3, 1:3, 2:4, 3:5, 4:6, 5:6, 6:7, 7:8, 8:9, 9:9, 10:10, 11:11, 12:12, 13:12, 14:13, 15:14, 16:15, 17:15, 18:1, 19:11, 20:12}
                elif attackType == AttackStyle.T_SPIN_MINI_DOUBLE:
                    attackDic = {0:2, 1:2, 2:3, 3:3, 4:4, 5:4, 6:5, 7:5, 8:6, 9:6, 10:7, 11:7, 12:8, 13:8, 14:9, 15:9, 16:10, 17:10, 18:11, 19:11, 20:12}
                elif attackType == AttackStyle.T_SPIN_DOUBLE:
                    attackDic = {0:5, 1:6, 2:7, 3:8, 4:10, 5:11, 6:12, 7:13, 8:15, 9:16, 10:17, 11:18, 12:20, 13:21, 14:22, 15:23, 16:25, 17:26, 18:27, 19:28, 20:30}
                elif attackType == AttackStyle.T_SPIN_TRIPLE:
                    attackDic = {0:7, 1:8, 2:10, 3:12, 4:14, 5:15, 6:17, 7:19, 8:21, 9:22, 10:24, 11:26, 12:28, 13:29, 14:31, 15:33, 16:35, 17:36, 18:38, 19:40, 20:42}
            elif B2B_Level == 2:
                if attackType == AttackStyle.QUAD:
                    attackDic = {0:6, 1:7, 2:9, 3:10, 4:12, 5:13, 6:15, 7:16, 8:18, 9:19, 10:21, 11:22, 12:24, 13:25, 14:27, 15:28, 16:30, 17:31, 18:33, 19:34, 20:36}
                elif attackType == AttackStyle.T_SPIN_MINI_SINGLE:
                    attackDic = {0:2, 1:2, 2:3, 3:3, 4:4, 5:4, 6:5, 7:5, 8:6, 9:6, 10:7, 11:7, 12:8, 13:8, 14:9, 15:9, 16:10, 17:10, 18:11, 19:11, 20:12}
                elif attackType == AttackStyle.T_SPIN_SINGLE:
                    attackDic = {0:4, 1:5, 2:6, 3:7, 4:8, 5:9, 6:10, 7:11, 8:12, 9:13, 10:14, 11:15, 12:16, 13:17, 14:18, 15:19, 16:20, 17:21, 18:22, 19:23, 20:24}
                elif attackType == AttackStyle.T_SPIN_MINI_DOUBLE:
                    attackDic = {0:3, 1:3, 2:4, 3:5, 4:6, 5:6, 6:7, 7:8, 8:9, 9:9, 10:10, 11:11, 12:12, 13:12, 14:13, 15:14, 16:15, 17:15, 18:1, 19:11, 20:12}
                elif attackType == AttackStyle.T_SPIN_DOUBLE:
                    attackDic = {0:6, 1:7, 2:9, 3:10, 4:12, 5:13, 6:15, 7:16, 8:18, 9:19, 10:21, 11:22, 12:24, 13:25, 14:27, 15:28, 16:30, 17:31, 18:33, 19:34, 20:36}
                elif attackType == AttackStyle.T_SPIN_TRIPLE:
                    attackDic = {0:8, 1:10, 2:12, 3:14, 4:16, 5:18, 6:20, 7:22, 8:24, 9:26, 10:28, 11:30, 12:32, 13:34, 14:36, 15:38, 16:40, 17:42, 18:44, 19:46, 20:48}
            elif B2B_Level == 3:
                if attackType == AttackStyle.QUAD:
                    attackDic = {0:7, 1:8, 2:10, 3:12, 4:14, 5:15, 6:17, 7:19, 8:21, 9:22, 10:24, 11:26, 12:28, 13:29, 14:31, 15:33, 16:35, 17:36, 18:38, 19:40, 20:42}
                elif attackType == AttackStyle.T_SPIN_MINI_SINGLE:
                    attackDic = {0:3, 1:3, 2:4, 3:5, 4:6, 5:6, 6:7, 7:8, 8:9, 9:9, 10:10, 11:11, 12:12, 13:12, 14:13, 15:14, 16:15, 17:15, 18:1, 19:11, 20:12}
                elif attackType == AttackStyle.T_SPIN_SINGLE:
                    attackDic = {0:5, 1:6, 2:7, 3:8, 4:10, 5:11, 6:12, 7:13, 8:15, 9:16, 10:17, 11:18, 12:20, 13:21, 14:22, 15:23, 16:25, 17:26, 18:27, 19:28, 20:30}
                elif attackType == AttackStyle.T_SPIN_MINI_DOUBLE:
                    attackDic = {0:4, 1:5, 2:6, 3:7, 4:8, 5:9, 6:10, 7:11, 8:12, 9:13, 10:14, 11:15, 12:16, 13:17, 14:18, 15:19, 16:20, 17:21, 18:22, 19:23, 20:24}
                elif attackType == AttackStyle.T_SPIN_DOUBLE:
                    attackDic = {0:7, 1:8, 2:10, 3:12, 4:14, 5:15, 6:17, 7:19, 8:21, 9:22, 10:24, 11:26, 12:28, 13:29, 14:31, 15:33, 16:35, 17:36, 18:38, 19:40, 20:42}
                elif attackType == AttackStyle.T_SPIN_TRIPLE:
                    attackDic = {0:9, 1:11, 2:13, 3:15, 4:18, 5:20, 6:22, 7:24, 8:27, 9:29, 10:31, 11:33, 12:36, 13:38, 14:40, 15:42, 16:45, 17:47, 18:49, 19:51, 20:54}
            else:
                if attackType == AttackStyle.QUAD:
                    attackDic = {0:8, 1:10, 2:12, 3:14, 4:16, 5:18, 6:20, 7:22, 8:24, 9:26, 10:28, 11:30, 12:32, 13:34, 14:36, 15:38, 16:40, 17:42, 18:44, 19:46, 20:48}
                elif attackType == AttackStyle.T_SPIN_MINI_SINGLE:
                    attackDic = {0:4, 1:5, 2:6, 3:7, 4:8, 5:9, 6:10, 7:11, 8:12, 9:13, 10:14, 11:15, 12:16, 13:17, 14:18, 15:19, 16:20, 17:21, 18:22, 19:23, 20:24}
                elif attackType == AttackStyle.T_SPIN_SINGLE:
                    attackDic = {0:6, 1:7, 2:9, 3:10, 4:12, 5:13, 6:15, 7:16, 8:18, 9:19, 10:21, 11:22, 12:24, 13:25, 14:27, 15:28, 16:30, 17:31, 18:33, 19:34, 20:36}
                elif attackType == AttackStyle.T_SPIN_MINI_DOUBLE:
                    attackDic = {0:5, 1:6, 2:7, 3:8, 4:10, 5:11, 6:12, 7:13, 8:15, 9:16, 10:17, 11:18, 12:20, 13:21, 14:22, 15:23, 16:25, 17:26, 18:27, 19:28, 20:30}
                elif attackType == AttackStyle.T_SPIN_DOUBLE:
                    attackDic = {0:8, 1:10, 2:12, 3:14, 4:16, 5:18, 6:20, 7:22, 8:24, 9:26, 10:28, 11:30, 12:32, 13:34, 14:36, 15:38, 16:40, 17:42, 18:44, 19:46, 20:48}
                elif attackType == AttackStyle.T_SPIN_TRIPLE:
                    attackDic = {0:10, 1:12, 2:15, 3:17, 4:20, 5:22, 6:25, 7:27, 8:30, 9:32, 10:35, 11:37, 12:40, 13:42, 14:45, 15:47, 16:50, 17:52, 18:55, 19:57, 20:60}

        damage = attackDic.get(combo, None)
        return damage
