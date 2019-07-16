# _*_ coding:utf-8 _*_
# @time     :  0:25
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : project_path.py
import os
#文件路径  放这里
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# print(project_path)

#测试用例的路径
case_path=os.path.join(project_path,'test_cases','test_api.xlsx')
print(case_path)

case_conf=os.path.join(project_path,'test_cases','case_id.conf')
print(case_conf)