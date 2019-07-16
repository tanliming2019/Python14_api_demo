# _*_ coding:utf-8 _*_
# @time     :  19:25
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : homework_1.py

# 1、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5 
def judge_len(*args):
    for a in args:
        if isinstance(a,str):#判断a是不是字符串类型
            if len(a)>5:
                print('参数：{}长度大于5'.format(a))
            else:
                print('参数：{}长度不大于5'.format(a))
        elif isinstance(a,list):#判断a是不是列表类型
            if len(a) > 5:
                print('参数：{}长度大于5'.format(a))
            else:
                print('参数：{}长度不大于5'.format(a))
        elif isinstance(a,tuple):#判断a是不是元组类型
            if len(a) > 5:
                print('参数：{}长度大于5'.format(a))
            else:
                print('参数：{}长度不大于5'.format(a))
        else:
            print('该函数不支持参数：{}的判断'.format(a))
judge_len([1,1],'wo',34)