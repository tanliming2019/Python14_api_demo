# _*_ coding:utf-8 _*_
# @time     :  0:44
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : run_2.py
import unittest
from ddt import ddt,data,unpack
from API_2_作业练习.common.http_request import HttpRequest
from API_2_作业练习.common.do_excle import DoExcle
from API_2_作业练习.common import project_path
from API_2_作业练习.common.my_logging import ReadLogging
from API_2_作业练习.common.get_caseid import DataType
result=DataType(project_path.case_conf).get_data('Case','id')
test_data=DoExcle(project_path.case_path,'test_case',result).read_data()#读取测试用例

@ddt
class TestCase(unittest.TestCase):
    def setUp(self):
        ReadLogging().info('---开始执行测试---')#开始准备工作
    def tearDown(self):
        ReadLogging().info('---测试执行完毕---')#清场工作，清除测试环境
    @data(*test_data)
    @unpack
    def test_001(self,Caseid,Module,Title,Url,Method,Params,ExpectedResult):
        print('-----正在测试{}模块第{}条用例：{}'.format(Module,Caseid,Title))
        resp=HttpRequest().http_request(Method,Url,eval(Params))
        a=resp.json()
        b=eval(ExpectedResult)
        global TestResult
        try:
            self.assertEqual(a,b)
            TestResult='Pass'
            ReadLogging().info('测试结果是：{}'.format(TestResult))
        except AssertionError as e:
            TestResult='Fail'
            ReadLogging().error('测试结果是：{}'.format(TestResult))
            raise e
        finally:
            #写回测试结果
            t=DoExcle(project_path.case_path,'test_case',result)
            t.write_back(Caseid+1,8,resp.text)
            t.write_back(Caseid+1,9,TestResult)









