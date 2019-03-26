# ==================================================================== 
# 类就是一系列有着共同特征事物的抽象体现
class Cocacola:
    formula=['caffeine','sugar','water','soda']

# 类似于赋值的操作就是类的实例化
coke_for_me = Cocacola()
coke_for_you = Cocacola()

print(coke_for_me.formula)
print(coke_for_you.formula)