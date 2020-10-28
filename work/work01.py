# 定义一个字典变量, 内容为 {"id": 10, "name": "周瑜", "age": 30}
dict1 = {"id": 10, "name": "周瑜", "age": 30}
print(dict1)
# 要求: 添加键值对 ”sex”:  ”男”, 再将 age 的值修改为 25, 最后遍历显示字典中所有的键和值
dict1['sex'] = '男'
print(dict1)
dict1['age'] = 25
print(dict1)
for i in dict1.items():
    print(i)
