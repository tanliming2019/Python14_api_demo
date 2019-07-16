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
from API_5.common import project_path
from API_5.common.get_data import GetData


#测试投资
test_data=DoExcle(project_path.case_path,'invest').read_data('InvestCASE')
my_log=ReadLogging()
COOKIE=None#设定COOKIES的初始值为None
@ddt
class TestCase(unittest.TestCase):
    def setUp(self):#测试之前的准备工作
        self.t=DoExcle(project_path.case_path,'invest')#写入测试结果的对象
        pass

    def teaDown(self):
        pass


    #写测试用例
    @data(*test_data)
    def test_case(self,case):
            global TestResult#全局变量
            global COOKIES #声明全局变量
            method=case['Method']
            url=case['Url']
            param=eval(case['Params'])
            # 发起测试
            my_log.info('-----正在测试{}模块第{}条用例：{}'.format(case['Module'], case['CaseId'], case['Title']))
            my_log.info('测试数据是：{}'.format(case))
            resp=HttpRequest().http_request(method, url, param,cookies=getattr(GetData,'COOKIE'))#http_request模块已经做了异常处理，所以在这里不用再做
            #加一个判断
            if resp.cookies:#判断请求的cookies是否为空  不为空其实就是True
                setattr(GetData,'COOKIE',resp.cookies)#我们可以更新COOKIES这个全局变量的值
            try:
                self.assertEqual(eval(case['ExpectedResult']), resp.json())
                TestResult = 'Pass'  # 请注意这里
            except AssertionError as e:
                TestResult = 'Failed'
                my_log.error('http请求测试用例出错了，错误是：{}'.format(e))
                raise e  #处理完异常之后要抛出去 raise
            finally:
                #写回测试结果
                self.t.write_back(case['CaseId']+1,9,resp.text)
                self.t.write_back(case['CaseId']+1,10,TestResult)
            my_log.info('实际结果:{}'.format(resp.json())) # http发送请求拿到的实际返回值
            my_log.info('期望结果：{}'.format(eval(case['ExpectedResult'])))


