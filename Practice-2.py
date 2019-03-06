# 设计一个函数，在桌面的文件夹上创建10个文本，以数字给他们命名。

# 方法-1: 使用while循环
def creatFeil(feilNum):
    while feilNum > 0:
        root_path = "c://Users//FE/Desktop/"
        feil_path = str(feilNum)+'.txt'
        complete_path = root_path + feil_path
        open(complete_path,'w')
        feilNum = feilNum -1

# creatFeil(10)

# 方法-2: 使用for循环
def creatFeil2(feilNum):
    for x in feilNum:
        root_path = 'c://Users/FE/Desktop/'
        feil_path = str(x) + '.txt'
        complete_path = root_path + feil_path
        open(complete_path,'w')

# creatFeil2(range(1,11))



# 设计一个复利计算函数 invest()，他包含三个参数：amount(资金),rate(利率),time(投资时间)。输入每个参数后调用函数，应该返回每一年的资金总额。

def invest(amount,rate,time):
    print('复利函数')
    # year = None
    # amount_num = None
    for x in time:
        year = '第' + str(x) + '年:'
        amount_num = amount*(rate/100)+amount
        amount = amount_num
        print(year,str(amount_num))

invest(100000,7,range(1,11))



# 打印1~100内的偶数

def getOdd(number_range=range(1,101)):
    for x in number_range:
        if(x % 2 == 0):
            print(x)

# getOdd()