# _*_ coding:utf-8 _*_
# @time     :  22:45
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : add.py

def add_1(a,b):
    '完成a+b的函数'
    return a+b


def add_2(*args):
    sum=0
    for item in args:
        sum+=item
    return sum



def add_five_number(a,b,c,d,e,):
    print(a+b+c+d+e)


if __name__ == '__main__':
    print(add_2(1,2,3,4,5))
    print(add_five_number(222,2,2,22,2))