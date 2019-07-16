# _*_ coding:utf-8 _*_
# @time     :  22:15
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : class_python文件处理.py
#
# file=open('test14.txt','w',encoding='utf-8')
# res=file.read(5)
#
# print(res)

# res=file.readline()

# for i in range(1,20):
#     res=file.readline()
#     if i == 3:
#         print(res)
#
# print(res)

# res=file.readlines()
# print(res)
file=open('test14.txt','a+',encoding='utf-8')


file.write('lengmom')
file.seek(3,0)
res=file.readlines()
print(res)