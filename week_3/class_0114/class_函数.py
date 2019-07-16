# _*_ coding:utf-8 _*_
# @time     :  0:44
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : class_函数.py

def send_msg(who,msg):
    '''完成发送短信的功能
       who 发送给谁
       msg 短信内容
    '''

    print('发送给{}，信息是{}'.format(who,msg))
    return 'huahua'
send_msg('华华','早上好!')
# print(send_msg('华华','早上好!'))#调用函数的同时，打印return返回的值
