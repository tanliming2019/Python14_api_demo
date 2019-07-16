# _*_ coding:utf-8 _*_
# @time     :  15:53
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : class_函数知识补充.py

#
# def talk_to_teacher(msg):
#     print('跟华华老师说：{}'.format(msg))
#
# def send_msg(tel,msg):
#     print('发送给{},{}'.format(tel,msg))
#
#
#
# talk_to_teacher('上课上到什么时候')
#
# send_msg('1501313142','五月底')


#msg='全局变量：Python14期的秀儿是跳坑王'
def send_msg():

    global msg
    msg='局部变量：华华是个挖坑王'
    print('发送的消息是:{}'.format(msg))
    msg='华华是个挖坑王,Python14期的秀儿是跳坑王'
send_msg()


def talk_to_teacher():
    print('跟老师交谈的内容是：{}'.format(msg))

talk_to_teacher()
print(msg)