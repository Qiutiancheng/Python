# 设计一个小游戏猜大小，游戏流程是：游戏开始时，选择big或者small。选择完成后开始摇骰子，11<=总值<=18为big，3<=总值<=10为small。然后告诉玩家才对或者猜错

# 引入一个生成随机数的内置库
import random

# 生成三个筛子
point1 = random.randrange(1,7)
point2 = random.randrange(1,7)
point3 = random.randrange(1,7)

# 计算总值，根据总值及押注计算游戏结果
point_list = [point1,point2,point3]
def getResult(pointAmount = sum(point_list)):
    big = 11 <= pointAmount <=18
    small = 3 <= pointAmount <= 10
    if big:
        return 'big'
    elif small:
        return 'small'

def start_game():
    # 游戏可选答案
    answers = ['big','small']
    # 玩家答案，自带防呆设计
    bet = input('Please select the size(big or small):').lower()
    # 游戏答案
    result = getResult()
    # 胜利条件
    win = bet == result
    # 判断输入的答案是否存在
    if bet in answers:
        # 判断玩家是否胜利
        if win:
            print('The points are',sum(point_list),'You Win!!!')
        else:
            print('The points are',sum(point_list),'You lose!!!')
    else:
        print('Please enter right answer(big ro small)')
        start_game()

start_game()
    
