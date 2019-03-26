# 数据结构
# ====================================================================
# List is a collection which is ordered and changeable. Allows duplicate members.

# 查
newList = ['马冬梅']
# print(newList[0])

# 增，第一个参数为插入参数（什么冬梅）的索引。如果索引大于列表的长度，则会放在列表的最后一个。
newList.insert(1,'什么冬梅')
# print(newList[1])

# 删,有两种方法
# newList.remove('什么冬梅') # 方法一
# del newList[0] # 方法二
# print(newList)


# 改
newList[0] = '马什么梅'
# print(newList)


#  ====================================================================
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

newDic = {
    'people1':'马冬梅',
    'people2':'什么东梅',
    'people3':'马东什么',
    'people4':'马什么梅'
}

# 查
# print(newDic['people1'])

# 增
newDic['people5'] = '大爷' # 添加单个元素
# print(newDic['people5'])

newDic.update({'people6':'大哥','people7':'大嫂'}) # 添加多个元素
# print(newDic)

# 删
del newDic['people1'] 
# print(newDic)



# ====================================================================
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

newTuple = ('a','b','c','d','e','f','g')
# print(newTuple[0])



# ====================================================================
# Set is a collection which is unordered and unindexed. No duplicate members.
newSet = {1,2,3,4,4}
newSet.add(5)
newSet.discard(5)
# print(newSet)



# ==================================================================== 
# 数据结构的一些技巧
num_list = [1,4,6,9,23,11]
# sorted方法可以给列表排序，设置reverse参数后按照倒序排列
sort_list = sorted(num_list,reverse=True)
# print(sort_list)



# ==================================================================== 
# 列表解析式/推导式
list_push = [i for i in range(1,11)]
print(list_push)