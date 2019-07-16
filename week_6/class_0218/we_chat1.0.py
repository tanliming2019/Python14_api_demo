# _*_ coding:utf-8 _*_
# @time     :  21:58
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : we_chat1.0.py
from week_6.class_0218.we_Chat import WeChat
class WeChat_1(WeChat):
    def send_red_bag(self,money,numbers=1,stat=1):#发红包
        '''money:发红包总金额
        numbers:红包个数  1:1个  X：指定个数
        stat:状态  1：表示平分  2：表示随机'''
        if 0.01<=money<=200:
            if numbers!=1:#发送多个
                print('共发送{}个红包，每个红包金额{}元'.format(numbers,money/numbers))
            else:
                print('发送一个红包，金额是{}元'.format(money))
        else:
            print('红包金额必须在0.01-200元之间')


p=WeChat_1()
p.send_red_bag(20,10,1)