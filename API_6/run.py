# _*_ coding:utf-8 _*_
# @time     :  2:26
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : run.py
#执行用例 生成测试报告
import sys
sys.path.append('./')
print(sys.path)
import unittest
import HTMLTestRunnerNew
from API_6.common import project_path
from API_6.test_cases import test_register#具体到模块
from API_6.test_cases import test_recharge

#新建一个测试集
suit=unittest.TestSuite()

#添加测试用例
loader=unittest.TestLoader()
suit.addTest(loader.loadTestsFromModule(test_register))
suit.addTest(loader.loadTestsFromModule(test_recharge))
#执行测试用例 生成测试报告
with open(project_path.report_path,'wb')as fail:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=fail,
                                            verbosity=2,
                                            title='python14测试报告',
                                            description='20190619_python14测试报告',
                                            tester='谭利明')
    runner.run(suit)#传入suit suit里面是我们收集的测试用例

