# 定义字典数据
dict1 = {'name': '刘备', 'age': 45, 'title': '君主'}
print(dict1)
# 增加
# 作用：给字典数据增加新的键值对
# 语法：字典名['键名'] = 键值
dict1['weapon'] = '双股剑'
print(dict1)

# 删除
# 作用：将指定的键和值移除
# 语法：del 字典名['键名']
del dict1['age']
print(dict1)
# 如果不指定键名，则会删除整个字典数据，在调用时会报错

# 清空
# 作用：清空字典数据
# 语法：字典名.clear()
# dict1.clear()
# print(dict1)

# 修改
# 作用：修改字典中已存在的数据
# 语法：字典名['已存在键名'] = 键值
dict1['title'] = '丞相'
print(dict1)
list1 = []
print(list1)
list1.append(dict1)
print(list1)

# 键值对形式数据，一般要求键不能重复，
# 如果键存在会更新旧值，如果键不存在，则新增数据


# 查找
# 通过键名
# 语法：字典名['键名']
print(dict1['name'])
# 该方法查询不存在的键名时，代码会报错
# print(dict1['age'])  # KeyError: 'age'

# 通过get查找
# 作用：返回键名对应的值
# 语法：字典名.get（'键名'）
print(dict1.get('name'))
# 注意：该方法查询不存在的键名时，
# 代码不会报错，而是返回None（没有数据）
print(dict1.get('age'))












