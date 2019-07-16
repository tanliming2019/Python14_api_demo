# _*_ coding:utf-8 _*_
# @time     :  0:32
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : learn_suit.py

import unittest
from week_7.class_0301.class_unittest_learn import *
#添加用例
suite=unittest.TestSuite()#测试套件--收集/存储用力
suite.addTest(TestAdd('test_001'))  
suite.addTest(TestAdd('test_002'))
suite.addTest(TestAdd('test_003'))
suite.addTest(TestAdd('test_004'))
suite.addTest(TestSub('test_two_postive'))

#执行测试用例   TestTextRunner
with open('test.txt','w',encoding='utf-8') as file:
    runner=unittest.TextTestRunner(stream=file,verbosity=2)
    runner.run(suite)


