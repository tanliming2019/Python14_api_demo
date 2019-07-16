# _*_ coding:utf-8 _*_
# @time     :  16:56
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : class_math_method.py

class Math_Method:
    '''这是一个数学类，里面包含各种数学方法'''
    c=10
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        '加法'
        return self.a+self.b+self.c

    @classmethod  #类函数
    def sub(cls):
        return cls.c+10

    @staticmethod  #静态函数
    def div():
        return 10

if __name__ == '__main__':#测试代码

    t=Math_Method(4,5)#创建一个对象
    res=t.add()
    print(res)


