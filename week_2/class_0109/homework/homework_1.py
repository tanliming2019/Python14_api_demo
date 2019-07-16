# _*_ coding:utf-8 _*_
# @time     :  21:09
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : homework_1.py


# 1.利用while循环 完成1-100的整数数字相加和
#方法一
a=0#定义变量
b=0
while a<=100:
    b=b+a
    a=a+1
print(b)

#方法二
sum=0#求和
a=0
while True:#永真式
    a+=1
    sum+=a
    print(a)
    if a==100:
        break
print(sum)

