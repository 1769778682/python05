# 需求1：定义函数能够打印一条有*构成的分割线
def print_line1():
    print('*' * 50)


# 需求2：定义函数能够打印一条由任意字符组成的分割线
def print_line2(char):  # 只要是不能够写死的数据，那么一定要使用参数
    print(char * 50)


# 需求3：定义函数能够打印一条由任意字符，任意个数，组成的分割线
def print_line3(char, num):
    print(char * num)


# 函数调用
# print_line1()
# print_line2('<')
# print_line3('.', 30)


# 需求：定义一个打印5行分割线，并且分割线的要求符合需求3
def print_line4(char, mum, b):
    raw = 0
    while raw < b:
        print_line3(char, mum)
        raw += 1


# 函数调用
# print_line4('《', 30, 7)