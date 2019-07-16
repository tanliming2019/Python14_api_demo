# _*_ coding:utf-8 _*_
# @time     :  22:31
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : homework_1.py

# 1：人和机器猜拳游戏写成一个类，有如下几个函数：
# # # 1）函数1：选择角色1 曹操 2张飞 3 刘备
# # # 2）函数2：角色猜拳1剪刀 2石头 3布 玩家输入一个1-3的数字
# # # 3）函数3：电脑出拳 随机产生1个1-3的数字，提示电脑出拳结果
# # # 4）函数4：角色和机器出拳对战，对战结束后，最后出示本局对战结果...赢...输,然后提示用户是否继续？按y继续，按n退出。
# # # 5）最后结束的时候输出结果 角色赢几局 电脑赢几局，平局几次 游戏结束



class Game:

    '''这是一个猜拳游戏类'''
    #函数1
    def Selec_Role(self):#选择角色
        dict_1 = {'1': '曹操', '2': '张飞', '3': '刘备'}
        while True:
            num=input('请输入角色编号(1曹操 2张飞 3刘备):')
            if num in dict_1.keys():
                print('选择的角色为{}'.format(dict_1[num]))
                return dict_1[num]
            else:
                print('请选择正确的角色')
                continue


     #函数2
    def Role_Finger_Guessing(self):#角色出拳
        global dict_2
        dict_2 = {'1': '剪刀', '2': '石头', '3': '布'}
        while True:
            r_play_num=input('角色出拳(1剪刀 2石头 3布):')

            if r_play_num in dict_2.keys():
                print('角色出拳是：',dict_2[r_play_num])
                return r_play_num
            else:
                print('出拳错误，请重新出拳')
                continue

    #函数3
    def Computer_Finger_Guessing(self):#电脑出拳
        import random
        c_play_num=str(random.randint(1, 3))
        print('电脑出拳：',dict_2[c_play_num])
        return c_play_num
    #函数4
    @classmethod
    def Game_begin(cls):#角色和电脑对战
        count_1=0 #平局次数
        count_2=0 #角色赢次数
        count_3=0 #电脑赢次数
        who=P.Selec_Role() #who 选择角色
        r=int(P.Role_Finger_Guessing())# r 角色出拳返回的结果
        c=int(P.Computer_Finger_Guessing()) # c 电脑出拳返回的结果

        if r==c:#平局
            print('平局,请问是否继续？（按y继续，按n退出）')
            count_1+=1 #平局次数累计
            while True:
                asking=input('请输入：y/n') #询问是否继续

                if asking == 'n':
                    print('角色赢{}次，电脑赢{}次，平局{}次,游戏结束'.format(count_2,count_3,count_1))
                    break
                elif asking =='y':
                        P.Game_begin()
                else:
                    print('只能输入y/n')
                    continue

        elif r==1 and c==3:#角色胜
            print('{}胜，{}输'.format(who,'电脑'))
            count_2 += 1  #角色胜次数累计
            while True:
                asking = input('请输入：y/n')

                if asking == 'n':
                    print('角色赢{}次，电脑赢{}次，平局{}次,游戏结束'.format(count_2, count_3, count_1))
                    break
                elif asking == 'y':
                    P.Game_begin()
                else:
                    print('只能输入y/n')
                    continue

        elif r==2 and c==1:
            print('{}胜，{}输'.format(who, '电脑'))
            count_2 += 1

            while True:
                asking = input('请输入：y/n')
                if asking == 'n':
                    print('角色赢{}次，电脑赢{}次，平局{}次,游戏结束'.format(count_2, count_3, count_1))
                    break
                elif asking == 'y':
                    P.Game_begin()
                else:
                    print('只能输入y/n')
                    continue

        elif r==3 and c==2:
            print('{}胜，{}输'.format(who, '电脑'))
            count_2 += 1

            while True:
                asking = input('请输入：y/n')
                if asking == 'n':
                    print('角色赢{}次，电脑赢{}次，平局{}次,游戏结束'.format(count_2, count_3, count_1))
                    break
                elif asking == 'y':
                    P.Game_begin()
                else:
                    print('只能输入y/n')
                    continue

        elif c==1 and r==3:  #电脑胜
            print('{}胜，{}输'.format('电脑',who))
            count_3 += 1  #电脑胜次数累计

            while True:
                asking = input('请输入：y/n')
                if asking == 'n':
                    print('角色赢{}次，电脑赢{}次，平局{}次,游戏结束'.format(count_2, count_3, count_1))
                    break
                elif asking == 'y':
                    P.Game_begin()
                else:
                    print('只能输入y/n')
                    continue

        elif c==2 and r==1:
            print('{}胜，{}输'.format('电脑',who))
            count_3 += 1

            while True:
                asking = input('请输入：y/n')
                if asking == 'n':
                    print('角色赢{}次，电脑赢{}次，平局{}次,游戏结束'.format(count_2, count_3, count_1))
                    break
                elif asking == 'y':
                    P.Game_begin()
                else:
                    print('只能输入y/n')
                    continue

        elif c==3 and r==2:
            print('{}胜，{}输'.format('电脑',who))
            count_3 += 1

            while True:
                asking = input('请输入：y/n')
                if asking == 'n':
                    print('角色赢{}次，电脑赢{}次，平局{}次,游戏结束'.format(count_2, count_3, count_1))
                    break
                elif asking == 'y':
                    P.Game_begin()
                else:
                    print('只能输入y/n')
                    continue

if __name__ == '__main__':
    P=Game()
    P.Game_begin()