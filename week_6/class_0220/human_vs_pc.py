# _*_ coding:utf-8 _*_
# @time     :  1:55
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : human_vs_pc.py
import random
class Humanvspc:

    '''人机大战'''

    def __init__(self):
        self.fist_dict={'1':'剪刀','2':'石头','3':'布'}


    def choose_role(self):
        '''选择角色'''
        role_dict={'1':'曹操','2':'张飞','3':'刘备'}
        while True:
            num=input('请输入你要选择的角色：1 曹操 2 张飞 3 刘备')
            if num in role_dict.keys():
                print('获取的角色是{}'.format(role_dict[num]))
                return role_dict[num]
            else:
                print('输入的角色不存在，请重新选择')
                continue

    def human_fist(self):#角色出拳
        '''角色猜拳 1 剪刀 2 石头 3 布 请玩家输入1-3'''
        role=self.choose_role() #调用类里面其他函数  self.函数名
        while True:
            num=input('请出拳：1 剪刀 2 石头 3 布')
            if num in self.fist_dict.keys():
                print('{}出拳为：{}'.format(role,self.fist_dict[num]))
                return int(num)
            else:
                print('出拳错误，请重新出拳')
                continue


    def PC_fist(self):#电脑出拳
        '''电脑猜拳 1 剪刀 2 石头 3 布 请玩家输入1-3'''
        num=str(random.randint(1,3))
        print('Pc出拳为{}'.format(self.fist_dict[num]))
        return int(num)


    def human_vs_pc(self):#人机对战
        a = 0  # 记录角色赢的次数
        b = 0  # 记录电脑赢的次数
        c = 0  # 记录平局次数
        while True:
            humanfist=self.human_fist()
            pcfist=self.PC_fist()

            if humanfist-pcfist in (1,-2):#角色赢
                a+=1
                print('角色赢了')
            elif humanfist-pcfist in (-1,2):
                b+=1
                print('PC赢了')
            else:
                c+=1
                print('平局')

            choice=input('是否继续对战 y 继续  n 退出')
            if choice == 'y':
                continue
            else:
                break
        print('这次对战，角色赢{}局，电脑赢{}局，平局{}局'.format(a,b,c))

if __name__ == '__main__':
    p=Humanvspc()
    p.human_vs_pc()