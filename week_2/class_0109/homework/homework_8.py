# _*_ coding:utf-8 _*_
# @time     :  23:14
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : homework_8.py


# 8:求 0—7 所能组成的奇数个数
a=0#能组成奇数的个数
for i in range(0,77777778):#0,1,2,,3,4,5,6,7,range函数取头不取尾，取左不取右
    if '8' not in str(i) and '9'not in str(i):
        if i%2!=0:#除以2不等于0为奇数
            a+=1
print(a)


