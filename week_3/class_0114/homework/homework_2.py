# _*_ coding:utf-8 _*_
# @time     :  19:25
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : homework_1.py
# 2、写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回 
#方法一
def judge_len_2(*args):
    for b in args:#b从args那里取值
        if isinstance(b,list) and len(b)>2:#判断b是不是列表类型
            print(len(b))
            while len(b)>2:
                i=2 #i是列表的索引
                b.pop(i)#减去索引大于1的值
                i+=1
            return print('新的数据为{}'.format(b))
        elif isinstance(b,list) and len(b)<2:
            print('该数据{}长度小于2'.format(b))
        else:
            print('该数据{}不符合判断条件'.format(b))
judge_len_2(['wo',2,2,2,2,2,])




# 方法二
def judge_len_2(L):
    if isinstance(L,list):
        if len(L)>2:
            return print(L[0:2])#取头不取尾，取左不取右
        else:
            print('长度小于2')
    else:
        print('该数据类型不符合判断条件')

judge_len_2([1,121,1,112,2])