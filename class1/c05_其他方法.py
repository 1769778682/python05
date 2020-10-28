dict1 = {'name': '刘备', 'age': 45, 'title': '君主'}


# 其他方法
# keys
# 作用：将字典所有的键返回，存放于一个特殊的列表当中
# 语法：字典名.keys
print(dict1.keys())
# 遍历
for i in dict1.keys():
    print(i)

# values
# 作用：将字典所有的值返回，存放于一个特殊的列表当中
# 语法：字典名.values（）
print(dict1.values())
# 遍历
for j in dict1.values():
    print(j)

# items
# 作用：将字典中的每一个键值对处理成一个元组，在存放于列表当中
# 语法：dict1.items()
print(dict1.items())

# 遍历优化
for key, value in dict1.items():
    print(key, value)