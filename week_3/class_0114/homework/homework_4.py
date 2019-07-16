# _*_ coding:utf-8 _*_
# @time     :  19:28
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : homework_4.py

# 4、一个足球队在寻找年龄在x岁到y岁的小女孩（包括x岁和y岁）加入。
# 编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问k次后，输出满足条件的总人数。


def found_girls():
    x = 8 #假设符合加入条件最少年龄
    y = 14 #假设符合加入条件最大年龄
    k = 5  # 最多询问次数
    j = 0  # j是实时询问次数
    z = 0  # 满足条件的总人数
    while j<k:
        sex=input('请输入你的性别：')#m表示男性，f表示女性
        j+=1
        if sex == 'f':
            age = int(input('请输入你的年龄:'))
            if 8 <=age<= 14:
                print('欢迎你加入足球队')
                z+=1
            else:
                print('不好意思，你不符合加入的条件')
        else:
            print('不好意思，你不符合加入的条件')
    print('符合加入球队的总人数为：{}'.format(z))

found_girls()








