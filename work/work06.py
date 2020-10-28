# 定义一个函数 triangle_test()，
# 有三个参数 a, b, c, 判断三个数构成的三角形类型


def triangle_test(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print('等边三角形')
        elif a == b or a == c or b == c:
            print('等腰三角形')
        else:
            print('普通三角形')
    else:
        print('不是三角形')


triangle_test(4, 9, 7)