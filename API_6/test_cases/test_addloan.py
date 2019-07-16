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
from API_6.common import project_path
from API_6.common import get_data
from API_6.common.get_data import GetData
from API_6.common.do_mysql import DoMySql


#测试充值
test_data=DoExcle(project_path.case_path,'add_loan').read_data('AddLoanCASE')
my_log=ReadLogging()
COOKIE=None#设定COOKIES的初始值为None
@ddt
class TestCase(unittest.TestCase):
    def setUp(self):#测试之前的准备工作
        self.t=DoExcle(project_path.case_path,'add_loan')#写入测试结果的对象
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

            # #替换loan_id
            # if case['Params'].find('loanid')!=-1:
            #     param=eval(case['Params'].replace('loanid',str(getattr(GetData,'LOAN_ID'))))
            #                                            #因为拿到的值是int类型  replace的替换是字符串间的替换 所以要str()强转一下
            # else:
            #     param = eval(case['Params'])

            param=eval(get_data.replace(case['Params']))

            # 发起测试
            my_log.info('-----正在测试{}模块第{}条用例：{}'.format(case['Module'], case['CaseId'], case['Title']))
            my_log.info('测试数据是：{}'.format(case))
            resp=HttpRequest().http_request(method, url, param,cookies=getattr(GetData,'COOKIE'))#http_request模块已经做了异常处理，所以在这里不用再做

            #判断是否要查询数据库
            if case['Sql']!=None:#如果Sql语句不为None,那就是要进行数据库的查询操作
                loan_id=DoMySql().do_mysql(eval(case['Sql'])['sql'],1)#返回的是元组 下一个请求要用到loan_id  #eval()之后得到字典 再根据字典的key取值得到sql语句
                setattr(GetData,'loanid',str(loan_id[0])) #利用反射    loan_id返回的是元组，所以根据索引取第一个值  loan_id[0]为int类型


            #实实在在的http请求之后才去加一个判断，判断是否加cookies
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


