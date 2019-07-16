# _*_ coding:utf-8 _*_
# @time     :  17:32
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : test_register.py
import unittest
from ddt import ddt,data
from API_6.common.my_log import ReadLogging
from API_6.common.do_excle import DoExcle
from API_6.common.http_request import HttpRequest
from API_6.common.project_path import case_path
from API_6.common.get_data import GetData
from API_6.common.do_mysql import DoMySql


#测试充值
test_data=DoExcle(case_path,'recharge').read_data('RechargeCASE')
my_log=ReadLogging()
# COOKIES=None#设定COOKIES的初始值为None
@ddt
class TestCase(unittest.TestCase):
    def setUp(self):#测试之前的准备工作
        self.t=DoExcle(case_path, 'recharge')#写入测试结果的对象
        pass

    def teaDown(self):
        pass


    #写测试用例
    @data(*test_data)
    def test_case(self,case):
            global TestResult#全局变量
            # global COOKIES #声明全局变量
            method=case['Method']
            url=case['Url']
            param=eval(case['Params'])
            # 发起测试
            my_log.info('-----正在测试{}模块第{}条用例：{}'.format(case['Module'], case['CaseId'], case['Title']))
            my_log.info('测试数据是：{}'.format(case))

            # 充值前查询数据库获取余额，保存
            if case['Sql'] is not None:
                sql = eval(case['Sql'])['sql']
                before_amount = DoMySql().do_mysql(sql)[0]

            resp=HttpRequest().http_request(method, url, param,cookies=getattr(GetData,'COOKIE'))#http_request模块已经做了异常处理，所以在这里不用再做
            #加一个判断
            if resp.cookies:#判断请求的cookies是否为空  不为空其实就是True
                setattr(GetData,'COOKIE',resp.cookies)#我们可以更新COOKIES这个全局变量的值
            try:

                # 充值后查询数据库获取余额，保存
                if case['Sql'] is not None:
                    sql = eval(case['Sql'])['sql']
                    after_amount = DoMySql().do_mysql(sql)[0]
                    recharge_amount=int(param['amount'])#将充值金额转成int类型
                    expect_amount=before_amount+recharge_amount

                    self.assertEqual(expect_amount,after_amount)

                if case['ExpectedResult'].find('expectamount') > -1:#判断是否要做期望值的替换
                    case['ExpectedResult']=case['ExpectedResult'].replace('expectamount',str(expect_amount))

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



