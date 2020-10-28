# # 现有个人信息数据如下:
# person_info = [{"name": "刘备", "age": "45", "title": "蜀国君主"},
#                {"name": "张飞", "age": "40", "title": "右将军"},
#                {"name": "关羽", "age": "43", "title": "前将军"}]
# # 提示用户输入 "请输入要查询的名字:"
# name = input("请输入要查询的名字:")
# for i in range(len(person_info)):
#     name1 = person_info[i].get('name')
#     if name == name1:
#         print('姓名:', person_info[i].get('name'), ',',
#               '年龄:', person_info[i].get('age'), ',',
#               '官职:', person_info[i].get('title'))
# 例如:
# 如果输入刘备, 则打印输出: 姓名: 刘备, 年龄: 45, 官职: 蜀国君主
# 要求:
# 使用 for 循环实现
# 提示: 活用字典的 get() 方法
person_info = [{"name": "刘备", "age": "45", "title": "蜀国君主"},
               {"name": "张飞", "age": "40", "title": "右将军"},
               {"name": "关羽", "age": "43", "title": "前将军"}]
name = input("请输入要查询的名字:")
for i in person_info:
    if i.get('name') == name:
        print('姓名:', i.get('name'), '年龄:', i.get('age'), '官职:', i.get('title'))
