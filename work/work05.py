# 定义一个函数 sum_test(),
# 有一个参数 n，在函数中计算 1 + 2 + 3 + ... + n 的值，
# 并打印输出结果


def sum_test(n):
    sum1 = 0
    num = 0
    while num <= n:
        sum1 += num
        num += 1
    print(sum1)


sum_test(100)
