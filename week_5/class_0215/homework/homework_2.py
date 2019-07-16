# _*_ coding:utf-8 _*_
# @time     :  23:40
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : homework_1.py

# 2：依靠自己的想象力，编写一个软件测试工程师类，要求包含初始化函数 类函数 对象函数  静态函数

class STE:
    '''这是一个软件测试工程师类'''
    #初始化函数
    def __init__(self,age,skill,name):
        self.age=age
        self.skill=skill
        self.name=name
    #对象函数
    def job(self):
        print(self.name+'是一名自动化测试工程师,会使用的编程语言是'+self.skill)

    #类函数
    @classmethod
    def coding(cls):
        print('他今年'+cls('25岁','Python','谭利明').age)

    # #静态函数
    @staticmethod
    def information():
        print('在广州工作，2年的工作经验')


P=STE('25岁','Python','谭利明')#创建一个对象

P.job()#调用类的函数
P.coding()
P.information()