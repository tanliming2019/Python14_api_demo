# _*_ coding:utf-8 _*_
# @time     :  19:25
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : homework_1.py

# 3、定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，
# 如果字符串不在字典中，则添加到字典中，并返回新的字典。

def judge_3(a,b):#a是传入的字典，b是传入的字符串
    if isinstance(a,dict) and isinstance(b,str):#判断传入的参数a是传入的字典，b是传入的字符串
        if b not in a.values():
            a['new_x']=b #'new_x'是b的key
            return print(a)
        else:
            print('该字符串为字典里的值')
    else:
        print('传入的参数不符合判断要求')
judge_3({1:'2'},2)
