# # 将猜拳案例定义为一个函数
# import random
#
# computer = random.randint(1, 3)
#
#
# def play(n):
#     player = n
#     while True:
#         if 0 < player < 3:
#             if (player == 1 and computer == 2
#                     or player == 2 and computer == 3
#                     or player == 3 and computer == 1):
#                 print('啊哦')
#                 input('请输入您的数字:%d' % n)
#             else:
#                 print('嗯哼，小样！')
#                 input('请输入您的数字:%d' % n)
#         else:
#             print('您输入的数字不在范围内！')
#             input('请输入您的数字:%d' % n)
#         print('哎呦!猜中我心思啦')
#
# # 调用函数
# play(int(input('请输入您的数字:')))
