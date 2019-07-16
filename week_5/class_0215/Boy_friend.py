# _*_ coding:utf-8 _*_
# @time     :  23:17
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : Boy_friend.py

class Boy_Friend:

    #属性
    sex='男'
    age='18'
    height='180'
    weight='130'
    name='彭于晏'

    #函数
    def sport(self):
        #print('喜欢运动')
        print('打印self:',self)

    @classmethod
    def cook(cls):
        print('会做饭')

    def coding(self):
        print('会代码')

    @staticmethod
    def infor():
        print('个人信息')

#创建一个实例/对象
P=Boy_Friend()
# print('我男朋友的名字是'.format(P.name))
# P.sport()
# P.coding()
# print('打印对象：',P)
# P.sport()
P.infor()
Boy_Friend.infor()