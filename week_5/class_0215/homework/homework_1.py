# _*_ coding:utf-8 _*_
# @time     :  23:40
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : homework_1.py

# 1：编写一个数学类，要求初始化函数带a,b,c,d4个参数，然后有加减乘数四个函数

class Math:
    '''这是一个数学类'''
    a=10
    b=20
    c=30
    d=40
    #函数
    def add(self):#加法函数
        y1=P.a+P.b+P.c+P.d
        print('加法函数结果：',y1)

    def sub(self):#减法函数
        y2=P.d-P.c-P.b-P.a
        print('减法函数结果：',y2)

    def multiply(self):#乘法函数
        y3=P.a*P.b*P.c*P.d
        print('乘法函数结果：',y3)

    def divide(self):
        y4=P.d/P.c/P.b/P.a
        print('除法函数结果:',y4)

P=Math()#创建一个对象
P.add()
P.sub()
P.multiply()
P.divide()




