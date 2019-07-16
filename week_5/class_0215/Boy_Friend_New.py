# _*_ coding:utf-8 _*_
# @time     :  23:38
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : Boy_Friend_New.py
class Boy_Friend:
    def __init__(self,age,height,name):#初始化函数
        self.age=age
        self.height=height
        self.name=name

    #函数
    def sport(self,*args):
        print(self.name+'喜欢运动{}'.format(args))


    @classmethod
    def cook(cls):
        print(cls(22,180,'huahua').name+'会做饭')

    def coding(self):
        print('会代码')

    @staticmethod
    def infor():
        print('个人信息')

# #创建一个实例/对象
P=Boy_Friend(22,180,'胡歌')
P.sport('乒乓球','羽毛球')
Boy_Friend.cook()
