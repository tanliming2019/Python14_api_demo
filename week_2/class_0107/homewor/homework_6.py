# _*_ coding:utf-8 _*_
# @time     :  0:22
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : homework_6.py

# 6、生成随机整数，从1-9取出来。然后输入一个数字，来猜，如果大于，则打印bigger。小了，则打印less。如果相等，则打印equal
import random
a=random.randint(1,9)
b=input('请输入一个数字：')
if b.isdigit():
    b=int(b)
    if b>a:
        print('bigger')
    elif b<a:
        print('less')
    else:
        print('equal')
else:
    print('请输入整数')




