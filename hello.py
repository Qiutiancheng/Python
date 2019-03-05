import math
# define a function
def somthing (arg1,arg2):
    return 'Something'

# It's still work if you don't return
def PrintSomething (c):
    fahremheit = str(c * 9/5 + 32)
    print(fahremheit + '℉')
    
PrintSomething(17)

# G to KG
def toKilogram (v):
    kilogram = str(v/1000)
    return print(kilogram + 'KG')

toKilogram(500)

# get hypotenuse
def getHypotenuse (a,b):
    # 开根
    hypotenuse = math.sqrt(a * a + b * b)
    return print(hypotenuse)

getHypotenuse(3,4) 

# sep:The printed results are separated by the value of sep
print('   *','  * *',' * * *','   |   ',sep='\n')

# 写入一个文件，'w'参数表示如果没有该文件则创建一个，否则写入并覆盖文本内容
file = open('C://Users/FE/Desktop/TODO.txt','w')
file.write('hi')
