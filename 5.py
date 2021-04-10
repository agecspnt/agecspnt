"""
5.了解蒙蒂霍尔悖（bei）论的内容和游戏规则，采用函数的方法，编写程序模拟蒙蒂霍尔悖论游戏。
例如：假如你正参加一个有奖游戏节目，前方有3道门可以选择，其中一个后面是汽车，另外两个后面是山羊。
你选择一个门，例如1号门，主持人当然知道每个门后面是什么并且打开了另一个门，例如3号门，后面是一只山羊。
这时，主持人会问你：“你想改选2号门吗？”，然后根据你的选择确定最终要打开的门，并确定你获得山羊（输）或者汽车（赢）。
"""


def Monty_Hall_problem(x=10000):
    import random
    """1: 'car', 2: 'sheep', 3: 'sheep'"""
    win, win_else, cnt = 0, 0, 0  # 初始化

    ls = [1, 2, 3]  # 三扇门

    for i in range(x):
        # 模拟1w次循环
        cnt += 1  # 计数
        print(f"第{cnt}次模拟：")
        choice_player = random.choice(ls)  # 玩家随机选择一扇门
        print(f"    1.玩家选择了{choice_player}号门")

        if choice_player == 1:  # 判断主持人该选哪一扇门
            choice_leader = random.randint(2, 3)
        elif choice_player == 2:
            choice_leader = 3
        else:
            choice_leader = 2

        print(f'    2.主持人打开了{choice_leader}号门，并且门后是一只山羊')
        ls2 = [1, 2, 3]
        ls2.remove(choice_leader)  # 移除主持人选择的门
        print(f'    3.此时选手可选{ls2[0]}号门或{ls2[1]}号门')

        if choice_player == 1:  # 未改变选择
            win += 1
            print("    4.不改变选择赢了！", end='\n\n')

        ls2.remove(choice_player)
        choice_player = ls2[0]

        if choice_player == 1:  # 改变选择，选了另一个门
            win_else += 1
            print("    4.改变选择也赢了！", end='\n\n')

    print("模拟结果：")
    print(f'  *不改变选择的胜率为：{(win / 100)}%')
    print(f'  *改变选择的胜率为：{(win_else / 100)}%')


if __name__ == '__main__':
    Monty_Hall_problem()
