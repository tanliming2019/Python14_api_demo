# _*_ coding:utf-8 _*_
# @time     :  21:44
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : homework_3.py

# 3：利用for循环输出如下三角形
# *
# **
# *** 
# **** 
# ***** 
#方法1
a=1 #行数
b=' *'
while a<=5:
    print(b*a)
    a+=1

#方法2
while True:
    print(b*a)
    a+=1
    if a==6:#要打印5行，所以取6
        break

#方法3
for a in range(1,6):
    print('*'*a)