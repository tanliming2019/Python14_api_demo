# _*_ coding:utf-8 _*_
# @time     :  21:49
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : homework_4.py

# 4：请用嵌套for循环输出如下等边三角形（三个边均为5个*）
# #        *
# #      *   * 
# #    *   *   * 
# #  *  *    *   * 
#  *  *    *    *   * 


#方法一
for b in range(1,6):#1，2,3,4,5
    a=5-b
    print(" "*a+b*' *')


#方法二
for b in range(1,6):
    a=5-b
    print(a*' ',end='')#end=''不换行输出
    print(b*'* ')


#嵌套for循环方法
for a in range(1,6):
    for b in range(1,6-a):
        print('@',end='')
    print(' *'*a)