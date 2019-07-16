# _*_ coding:utf-8 _*_
# @time     :  0:32
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : learn_suit.py

import unittest
import HTMLTestRunnerNew
# from week_8.class_0304.class_unittest_learn import *
from week_8.class_0304 import class_unittest_learn
#添加用例
suite=unittest.TestSuite()#测试套件--收集/存储用例
# suite.addTest(TestAdd('test_001'))
# suite.addTest(TestAdd('test_002'))
# suite.addTest(TestAdd('test_003'))
# suite.addTest(TestAdd('test_004'))
# suite.addTest(TestSub('test_two_postive'))

loader=unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(TestAdd))#注意要看导入的是模块还是类
# suite.addTest(loader.loadTestsFromTestCase(TestSub))

suite.addTest(loader.loadTestsFromModule(class_unittest_learn))



#执行测试用例   TestTextRunner
# with open('test.txt','w', encoding='utf-8') as file:
#     runner=unittest.TextTestRunner(stream=file,verbosity=2)#老版本---生成测试报告
#     runner.run(suite)


with open('test.html','wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title='20190304测试报告_py14',
                                            description='2019年第一次报告',
                                            tester='阿明')
    runner.run(suite)