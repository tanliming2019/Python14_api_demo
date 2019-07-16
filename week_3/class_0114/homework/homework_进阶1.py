# _*_ coding:utf-8 _*_
# @time     :  22:55
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : homework_进阶1.py

# 进阶1：利用字符串所学内置函数，完成如下题目，具体使用的函数已经提示过了~在课堂上，请去视频里面找答案！
#
# 请用自己目前所学实现指定字符串大写转小写，小写变大写，
# 并且将字符串变为镜像字符串，镜像的意思是：大写的’A’变为’Z’,’大写的‘B‘变成‘Y,小写的’’’b’变为’y 。
# 目前要求处理的示范字符串是： ”sdSdsfdAdsdsdfsfdsdASDSDFDSFa” 需要提供至少2种不同的解决方法。

#方法一：
def change(x0):
    s_2=x0.swapcase()#字符串大写转小写，小写变大写
    print(s_2)
    x1=s_2.replace('A','Z')
    x2=x1.replace('B','Y')
    x3=x2.replace('b','y')
    print(x3)
change('sdSdsfdAdsdsdfsfdsdASDSDFDSFa')

#方法二：
def change(x0):
    for x1 in x0:
        if x1.islower():#判断是否小写
            x2=x1.upper()#小写转大写
            if x2=='A':#判断该字母是否为'A'
                x2='Z'
            elif x2=='B':#判断该字母是否为'B'
                x2='Y'
        else:
            x2=x1.lower()#大写转小写
            if x2=='b':#判断该字母是否为'b'
                x2='y'
        print(x2,end='')

change('sdSdsfdAdsdsdfsfdsdASDSDFDSFa')