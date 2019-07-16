# _*_ coding:utf-8 _*_
# @time     :  18:14
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : learn_ddt.py
import unittest
from ddt import ddt,data,unpack

# a=1,2,3
# @ddt#装饰测试类
# class TestPringMsg(unittest.TestCase):#继承
#     # @data([1,2,3],(4,5,9))
#     # def test_001(self,x):
#     #     print('我在执行第{}天'.format(x))
#     #     print('x:',x)
#     #     a=x[0]
#     #     b=x[1]
#     #     c=a+b
#     #     print('c:',c)


# @ddt#装饰测试类
# class TestPringMsg(unittest.TestCase):#继承
#     @data([1,2,3],(4,5,9))
#     @unpack
#     def test_001(self,a,b,expected):
#         print('我在执行第{}条测试用例'.format(a))
#
#         c=a+b
#         self.assertEqual(c,expected)


test_data=[[1,2,3],(4,5,9)]
test_data_2=[{'a':1,'b':2,'expected':3},{'a':3,'b':-2,'expected':1}]

# @ddt  # 装饰测试类
# class TestPringMsg(unittest.TestCase):  # 继承
#     @data(*test_data)
#     @unpack
#     def test_002(self,a,b,expected):
#         c=a+b
#         self.assertEqual(c,expected)

#
@ddt  # 装饰测试类
class TestPringMsg(unittest.TestCase):  # 继承
    @data(*test_data_2) #{'a':1,'b':2,'expected':3},{'a':3,'b':-2,'expected':1}
    @unpack
    def test_003(self,a,b,expected):
        c=a+b
        print(c)
        print(expected)
        self.assertEqual(c,expected)



@ddt  # 装饰测试类
class TestPringMsg(unittest.TestCase):  # 继承
    @data(*test_data_2) #{'a':1,'b':2,'expected':3},{'a':3,'b':-2,'expected':1}
    # @unpack
    def test_003(self,dict):
        c=dict['a']+dict['b']
        print(c)
        print(dict['expected'])
        self.assertEqual(c,dict['expected'])
































