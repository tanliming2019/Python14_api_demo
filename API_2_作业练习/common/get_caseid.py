# _*_ coding:utf-8 _*_
# @time     :  4:04
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : get_caseid.py
from configparser import ConfigParser
from API_2_作业练习.common.project_path import case_conf
class DataType:
    '''该类用于读取配置文件数据'''
    def __init__(self,file_name):
        self.cf=ConfigParser() #创建一个类对象
        self.cf.read(file_name,encoding='utf-8')#打开配置文件

    def get_data(self,section,option):
        res=self.cf.get(section,option)
        return eval(res)



if __name__ == '__main__':
    result = DataType(case_conf).get_data('Case','id')
    print(result)
    print(type(result))
