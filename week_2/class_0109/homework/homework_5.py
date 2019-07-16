# _*_ coding:utf-8 _*_
# @time     :  0:08
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : homework_5.py
# 5:输出99乘法表
a = 1
sum = 0
for i in range(1,10):#1,2,3,4......9
    for j in range(1,i+1):   #i:1  j:1   i:2  j:1,2
        sum = i*j
        print("{}x{}={}".format(i,j,sum),end="  ")   #end=''不换行
    print()



