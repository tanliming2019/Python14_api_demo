# _*_ coding:utf-8 _*_
# @time     :  21:46
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : we_Chat.py

class WeChat:
    '这是一个微信类'
    #属性
    year='2011'#微信产生的年份
    company='腾讯'#所属公司
    PM='张小龙'#产品经理
    #函数
    def add_friends(self):
        '''添加好友'''
        print('具有添加好友的功能')

    def send_msg(self):
        '发送信息'
        print('具有发送消息的功能')

t=WeChat()#对象
print(t.PM)#调用属性
t.send_msg()#调用函数
