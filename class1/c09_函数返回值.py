# 函数返回值return
name = '小明'
print(name)
name1 = name
print(name1)


def sum_(num1, num2):
    # 一般情况下，函数定义内部的所有数据，仅能在函数定义的内部使用    res = num1 + num2
    res = num1 + num2
    print(res)
    # 如果想要外界获取到函数内部的计算结果，需要通过return关键字将结果返回外界
    # 否则，函数调用处返回的结果为None
    return res
    # 注意：return 代表代码运行结束，表示返回结果，后续代码不会继续执行


# 调用函数
sum_(30, 49)
num = sum_(40, 30)  # 完全可以使用新变量接收函数调用
print(num)
