# 定义元组类型数据
tuple1 = (1, 2, 3, 4, 5, 6, 3, 3)
# 常用方法
# 通过索引值查找元素
# 语法：元组[索引]
print(tuple1[2])

# index
# 作用：返回目标数据的索引
# 语法：元组.index[目标数据]
print(tuple1[3])

# count
# 作用：统计目标数据出现的次数
# 语法：元组.count（目标数据）
print(tuple1[3])

# len
# 作用：返回目标元组的长度(数据个数)
# 语法：len（元组名）
print(len(tuple1))

# 注意：由于元组中的数据定义完成后，一般是不可变的，因此其对应的方法也比较少

name = '小明'
age = 20
print('%s今年%d岁了' % (name, age))
# 这种使用小括号包裹的多个变量, 属于元组数据类型的应用
