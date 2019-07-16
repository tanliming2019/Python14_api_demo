# _*_ coding:utf-8 _*_
# @time     :  0:04
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : 配置文件学习.py
from configparser import ConfigParser
#创建对象
cf=ConfigParser()
#打开文件 read()
cf.read('lemo.conf',encoding='utf-8')

#读取内容  section option
res=cf.get('StudentName','stu_3')
res=cf.getint('StudentName','stu_3')
print(res)
print(type(res))
# print(type(eval(res)))
