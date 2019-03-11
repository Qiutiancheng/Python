# 习题1：设计一个小游戏猜大小，游戏流程是：游戏开始时，玩家选择 big 或者 small，然后输入押注金额。选择完成后开始摇骰子，11<=总值<=18为big，3<=总值<=10为small。然后告诉玩家游戏结果。
# 初始游戏金额：1000
# 初始赔率：1倍
# 金额为0时游戏结束

import random
point1 = random.randrange(1,7)
point2 = random.randrange(1,7)
point3 = random.randrange(1,7)

init_money = 1000

point_list = [point1,point2,point3]

def GetResult():
    result = sum(point_list)
    big = 11 <= result <=18
    small = 3 <= result <= 10
    if big:
        return 'big'
    elif small:
        return 'small'

def StartGame():
    print('<<< 游戏开始 >>>','初始金额：1000','初始倍率：1',sep='\n')
    selects = ['big','small']
    user_select = input('请选择大小（big ro small）:').lower()
    user_pet = input('请下注:')
    not_enough = int(user_pet) > init_money
    error_option = user_select not in selects
    win = GetResult() == user_select
    if not_enough:
        print('筹码不足')
        return
    if error_option:
        print('没有该选项，请重新选择')
        StartGame()
    if win:
        # init_money = init_money + int(user_pet)
        print('点数为：',sum(point_list),'You Win!!!')
        print('获得',int(user_pet),'筹码','当前筹码:',init_money)
    else:
        # init_money = init_money - int(user_pet)
        print('点数为：',sum(point_list),'You Lose!!!')
        print('减少',int(user_pet),'筹码','当前筹码:',init_money)
        broken = (init_money - int(user_pet) <= 0)
        if broken:
            print('你破产了！')
            return

    

StartGame()