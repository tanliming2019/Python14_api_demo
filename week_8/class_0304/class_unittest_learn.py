# _*_ coding:utf-8 _*_
# @time     :  23:58
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : class_unittest_learn.py

import unittest
from ddt import ddt,data,unpack

test_data_1=[[1,2,3],[-1,2,1],[-1,-2,-3],[0,0,0]]

@ddt
class TestAdd(unittest.TestCase):#继承
    def setUp(self):#开始----每一条测试用例开始之情
        print('---开始执行测试----')#开始准备工作

    def tearDown(self):
        print('---测试执行完毕了---')#清场工作，清除测试环境

    # 写用例用test_开头
    @data(*test_data_1)  #[1,2,3],[-1,2,1],[-1,-2,-3],[0,0,0]
    def test_001(self,L):#两个整数相加
        a=L[0]
        b=L[1]
        expected=L[2]
        c=a+b
        try:
            self.assertEqual(expected, c)
        except AssertionError as e:
            print('001用例执行失败，错误是{}'.format(e))
            raise e
        print('测试结果：', c)

# @ddt
# class TestAdd(unittest.TestCase):  # 继承
#     def setUp(self):  # 开始----每一条测试用例开始之情
#         print('---开始执行测试----')  # 开始准备工作
#
#     def tearDown(self):
#         print('---测试执行完毕了---')  # 清场工作，清除测试环境
#
#     @data(test_data_1)  # [[1,2,3],[-1,2,1],[-1,-2,-3],[0,0,0]]
#     def test_001(self,x):  #----这是一个错误的示范，只穿了一个数给用例，执行了一条用例，因为for循环是在用例里面执行的
#         for item in x:
#             a=item[0]
#             b=item[1]
#             expected=item[2]
#             c=a+b
#             try:
#                 self.assertEqual(expected,c)
#             except AssertionError as e:
#                 print('001用例执行失败，错误是{}'.format(e))
#                 raise e
#             print('测试结果：',c)










    # def test_002(self):#一正一负相减
    #     a=-1
    #     b=2
    #     expected=1
    #     c=a+b
    #     try:
    #         self.assertEqual(expected, c)
    #     except AssertionError as e:
    #         print('002用例执行失败，错误是{}'.format(e))
    #         raise e
    #
    #
    # def test_003(self):#两个负数相减
    #     a=-1
    #     b=-2
    #     expected=-3
    #     c=a+b
    #     try:
    #         self.assertEqual(expected, c)
    #     except AssertionError as e:
    #         print('003用例执行失败，错误是{}'.format(e))
    #         raise e
    #
    # def test_004(self):#两个零相减
    #     a=0
    #     b=0
    #     expected=0
    #     c=a+b
    #     try:
    #         self.assertEqual(expected, c)
    #     except AssertionError as e:
    #         print('004用例执行失败，错误是{}'.format(e))
    #         raise e

    # class TestSub(unittest.TestCase):#继承
    #     def setUp(self):#开始----每一条测试用例开始之情
    #         print('开始执行测试')#开始准备工作
    #
    #     def tearDown(self):
    #         print('测试执行完毕了')#清场工作，清除测试环境
    #
    #
    #
    #     #写用例用test_开头
    #     def test_two_postive(self):#两个整数相减
    #         a=1
    #         b=2
    #         c=a-b
    #         print('测试结果是{}'.format(c))
    #
    #
    #     def test_postive_negative(self):#一正一负相减
    #         a=-1
    #         b=2
    #         c=a-b
    #         print('测试结果是{}'.format(c))
    #
    #
    #     def test_two_negative(self):#两个负数相减
    #         a=-1
    #         b=-2
    #         c=a-b
    #         print('测试结果是{}'.format(c))
    #
    #
    #     def test_two_zero(self):#两个零相减
    #         a=0
    #         b=0
    #         c=a-b
    #         print('测试结果是{}'.format(c))
