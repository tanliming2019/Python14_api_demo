# _*_ coding:utf-8 _*_
# @time     :  23:58
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : class_unittest_learn.py

import unittest
class TestSub(unittest.TestCase):#继承
    def setUp(self):#开始----每一条测试用例开始之情
        print('开始执行测试')#开始准备工作

    def tearDown(self):
        print('测试执行完毕了')#清场工作，清除测试环境


    #写用例用test_开头
    def test_two_postive(self):#两个整数相减
        a=1
        b=2
        c=a-b
        print('测试结果是{}'.format(c))


    def test_postive_negative(self):#一正一负相减
        a=-1
        b=2
        c=a-b
        print('测试结果是{}'.format(c))


    def test_two_negative(self):#两个负数相减
        a=-1
        b=-2
        c=a-b
        print('测试结果是{}'.format(c))


    def test_two_zero(self):#两个零相减
        a=0
        b=0
        c=a-b
        print('测试结果是{}'.format(c))




class TestAdd(unittest.TestCase):#继承
    def setUp(self):#开始----每一条测试用例开始之情
        print('开始执行测试')#开始准备工作

    def tearDown(self):
        print('测试执行完毕了')#清场工作，清除测试环境


    #写用例用test_开头
    def test_001(self):#两个整数相减
        a=1
        b=2
        expected=4
        c=a+b
        try:
            self.assertEqual(expected,c)
        except AssertionError as e:
            print('001用例执行失败，错误是{}'.format(e))
            raise e




    def test_002(self):#一正一负相减
        a=-1
        b=2
        expected=2
        c=a+b
        try:
            self.assertEqual(expected, c)
        except AssertionError as e:
            print('002用例执行失败，错误是{}'.format(e))
            raise e


    def test_003(self):#两个负数相减
        a=-1
        b=-2
        expected=1
        c=a+b
        try:
            self.assertEqual(expected, c)
        except AssertionError as e:
            print('003用例执行失败，错误是{}'.format(e))
            raise e

    def test_004(self):#两个零相减
        a=0
        b=0
        expected=1
        c=a+b
        try:
            self.assertEqual(expected, c)
        except AssertionError as e:
            print('004用例执行失败，错误是{}'.format(e))
            raise e