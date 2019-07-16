# _*_ coding:utf-8 _*_
# @time     :  22:53
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : homework_1.py

#写一个配置类 有以下几个函数： 
#1：读取整数
#2：读取浮点数 
#3：读取布尔值 
#4：读取其他类型的数据 list tuple dict eval（） 
#5：读取字符串
from configparser import ConfigParser
class Data_Type:
    '''读取数据类型的类'''
    def __init__(self,file_name):#

        self.cf=ConfigParser()  # 创建对象
        self.cf.read(file_name, encoding='utf-8') #打开配置文件

    def type_int(self,sesion,option):#读取整数
        res=self.cf.getint(sesion,option)
        return res

    def tyep_float(self,sesion,option):#读取浮点数
        res=self.cf.getfloat(sesion,option)
        return res

    def type_boolean(self,sesion,option):#读取布尔值
        res=self.cf.getboolean(sesion,option)
        return res

    def type_list(self,sesion,option):#读取列表
        res=self.cf.get(sesion,option)
        return eval(res)

    def type_str(self,sesion,option):
        res=self.cf.get(sesion,option)
        return res

if __name__ == '__main__':
    result=Data_Type('data_type.conf').type_list('DataType','type_4')
    print(result)
