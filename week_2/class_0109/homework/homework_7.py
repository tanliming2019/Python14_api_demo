# _*_ coding:utf-8 _*_
# @time     :  23:14
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : homework_7.py

#
# 7:有1 2 3 4 这四个数字，能组成多少个互不相同且无重复数字的三位数？分别是什么？ 
L=[]#空列表，用来存储数据
x=0 #记录符合条件的数据
a=[1,2,3,4]
for i in a:#百位
    for j in a:#十位
        for k in a:#个位
            if i !=j and j !=k and i!=k:
                y=j*100+i*10+k#互不相同且无重复数字的三位数
                L.append(y)
                x+=1
print(L)
print(x)









