# _*_ coding:utf-8 _*_
# @time     :  22:40
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : class_路径处理.py

# file=open('../../py14.txt',encoding='utf-8')
# print(file.read())


import os
# path_1=os.getcwd()
#
# path_2=os.path.realpath(__file__)
#
# path_3=os.path.basename(__file__)
#
# print(path_1)
# print(path_2)
# print(path_3)


# path_2=os.path.realpath(__file__)
# print(os.path.split(os.path.split(path_2)[0])[0])
# print(os.path.split(path_2))
path_2=os.path.realpath(__file__)
print('path_2:',path_2)

path_4=os.path.split(path_2)[0]
print('path_4:',path_4)

# path_5=os.path.join(path_4,'py14.txt')
# print('path_5:',path_5)

path_5=path_4+'/py14.txt'

file=open(path_5,encoding='utf-8')
print(file.read())
