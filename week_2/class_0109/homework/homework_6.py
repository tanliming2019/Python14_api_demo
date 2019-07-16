# _*_ coding:utf-8 _*_
# @time     :  23:12
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : homework_6.py

#
# 6:利用for循环，完成a=[1,7,4,89,34,2]的冒泡排序： 
# 冒泡排序：小的排前面，大的排后面。


a=[1,7,4,89,34,2]

for j in range(len(a)-1):#循环5次  0,1,2,3,4
        for i in range(len(a)-1):
            if a[i]>a[i+1]:   #前一个元素跟后一个元素比较，小的排前，大的排后
                a[i],a[i+1]=a[i+1],a[i]  #前一个元素跟后一个元素元素之前互换
        print(a)

