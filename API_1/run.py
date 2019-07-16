# _*_ coding:utf-8 _*_
# @time     :  2:26
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : run.py
from API_1.common.http_request import HttpRequest
from API_1.common.do_excle import DoExcle
from API_1.common import project_path
#完成用例的测试
#1、读取测试数据
test_data=DoExcle(project_path.case_path,'test_case').read_data()

#执行测试：遍历--根据key取值
for case in test_data:
    method=case['Method']
    url=case['Url']
    param=eval(case['Params'])
    #发起测试
    print('-----正在测试{}模块第{}条用例：{}'.format(case['Module'],case['Caseid'],case['Title']))
    resp=HttpRequest().http_request(method,url,param)
    print('实际结果:{}'.format(resp.json()))#http发送请求拿到的实际返回值
    print('期望结果：{}'.format(case['ExpectedResult']))


    #对比结果
    if resp.json()==eval(case['ExpectedResult']):
        TestResult='Pass'
    else:
        TestResult='Fail'
    print('该条用例测试结论{}:'.format(TestResult))


    #需要写回什么？实际结果/测试结论
    t=DoExcle(project_path.case_path,'test_case')
    t.write_back(case['Caseid']+1,8,resp.text)
    t.write_back(case['Caseid']+1,9,TestResult)
