# _*_ coding:utf-8 _*_
# @time     :  17:32
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : test_register.py
import unittest
from ddt import ddt,data
from API_5.common.my_log import ReadLogging
from API_5.common.do_excle import DoExcle
from API_5.common.http_request import HttpRequest
from API_5.common.project_path import case_path


#测试注册
test_data=DoExcle(case_path,'register').read_data('RegisterCASE')
my_log=ReadLogging()
COOKIES=None
@ddt
class TestCase(unittest.TestCase):
    def setUp(self):#测试之前的准备工作
        self.t=DoExcle(case_path, 'register')#写入测试结果的对象
        pass

    def teaDown(self):
        pass


    #写测试用例
    @data(*test_data)
    def test_case(self,case):
            global TestResult
            method=case['Method']
            url=case['Url']
            param=eval(case['Params'])
            # 发起测试
            my_log.info('-----正在测试{}模块第{}条用例：{}'.format(case['Module'], case['CaseId'], case['Title']))
            my_log.info('测试数据是：{}'.format(case))
            resp=HttpRequest().http_request(method, url, param,cookies=COOKIES)#http_request模块已经做了异常处理，所以在这里不用再做
            try:
                self.assertEqual(eval(case['ExpectedResult']),resp.json())
                TestResult='pass'
            except AssertionError as e:
                TestResult='Failed'
                my_log.error('请求测试用例出错，错误是{}'.format(e))
                raise e  #处理完异常之后要抛出去 raise
            finally:
                #写回测试结果
                self.t.write_back(case['CaseId']+1,8,resp.text)
                self.t.write_back(case['CaseId']+1,9,TestResult)
            my_log.info('实际结果:{}'.format(resp.json())) # http发送请求拿到的实际返回值
            my_log.info('期望结果：{}'.format(case['ExpectedResult']))



