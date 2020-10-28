# 定义分割线函数
def print_line():
    """分割线函数"""
    print('*' * 50)


# 调用函数
print_line()


# def say_hello():
#     print('*' * 50)
#     print('Hello Python')
#     print('*' * 50)
#
#
# # 调用函数
# say_hello()


def say_hello():
    print_line()  # 在一个函数定义内部，调用另一个函数，这就是函数嵌套
    print('Hello Python')
    print_line()


# 调用函数
say_hello()