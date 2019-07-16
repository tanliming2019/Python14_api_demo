# _*_ coding:utf-8 _*_
# @time     :  23:52
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : homework_3.py
# 3、输入一个数，判断一个数n能同时被3和5整除 

n=int(input('请输入一个能同时被3和5整除的数：'))
if n%3==0 and n%5==0:
    print('{}能被3和5整除'.format(n))
else:
    print('{}不能同时被3和5整除'.format(n))