# _*_ coding:utf-8 _*_
# @time     :  2:26
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : run.py
#执行用例 生成测试报告
import unittest
from API_3_作业练习.test_cases.test_cases import TestCase
from API_3_作业练习.common import project_path
import HTMLTestRunnerNew
#新建一个测试集
suit=unittest.TestSuite()

#添加测试用例
loader=unittest.TestLoader()
suit.addTest(loader.loadTestsFromTestCase(TestCase))

#执行测试用例 生成测试报告
with open(project_path.report_path,'wb')as fail:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=fail,
                                            verbosity=2,
                                            title='python14测试报告',
                                            description='20190619_python14测试报告',
                                            tester='谭利明')
    runner.run(suit)#传入suit suit里面是我们收集的测试用例

