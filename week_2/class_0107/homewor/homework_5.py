# _*_ coding:utf-8 _*_
# @time     :  0:14
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : homework_5.py

# 5、一个 5 位数，判断它是不是回文数。即 12321 是回文数，个位与万位相同，十位与千位相同。 根据判断打印出相关信息。
#
# a=input('请输入一个5位数：')
# if a[0]==a[4] and a[1]==a[3]:
#     print('{}是回文数'.format(a))
# else:
#     print('{}不是回文数'.format(a))


a=input('输入一个5位数:')
if len(a)==5 and a.isdigit():#判断是否为纯数字
    if a[0]==a[-1] and a[1]==a[-2] and a[0]!='0':#第一个数字开头不能为0
        print('{}是回文数'.format(a))
    else:
        print('{}不是回文数'.format(a))
else:
    print('输入有误，请输入5位数字')

