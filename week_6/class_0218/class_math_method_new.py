# _*_ coding:utf-8 _*_
# @time     :  17:21
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : class_math_method_new.py

from week_6.class_0218.class_math_method import Math_Method
class Math_Method_New(Math_Method):
    '这是一个数学类，里面包含各种数学方法'
    def add_args(self,*args):
        sum=0
        for item in args:
            sum+=item
        return print(sum)
if __name__ == '__main__':
    # res=Math_Method_New(4,5).add()
    # print(res)

    p=Math_Method_New(4,5)
    p.add_args(1,2,3)