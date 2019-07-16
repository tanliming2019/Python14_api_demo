# _*_ coding:utf-8 _*_
# @time     :  0:12
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : homework_1.py

# 1：编写一个日志类，能够实现输出文件到指定文件和console
# 2：结合配置文件类实现日志类的可配置，具体参考老师的代码以及视频
# 3：结合日志类以及do_excel类，加上异常判断 与日志输出
import logging
from week_7.class_0227.read_config import ReadConfig


class ReadLoging:

    def __init__(self):
        self.loging_name=ReadConfig('my_loging.conf').get_str('MyLoging','loging_name')
        self.loging_level=ReadConfig('my_loging.conf').get_str('MyLoging','loging_level')
        self.loging_formatter=ReadConfig('my_loging.conf').get_str('MyLoging','loging_formatter')


    def loging_1(self,level,msg):
        my_loging=logging.getLogger(self.loging_name)#定义日志收集器
        my_loging.setLevel(self.loging_level)#设置级别

        formatter=logging.Formatter(self.loging_formatter)
        ch=logging.StreamHandler()#指定输出渠道---控制台
        ch.setLevel(self.loging_level)#设置级别
        ch.setFormatter(formatter)#设置日志输出格式

        fh=logging.FileHandler('test_1.log',encoding='utf-8')#指定输入渠道---文件
        fh.setLevel(self.loging_level)#设置级别
        fh.setFormatter(formatter)  # 设置日志输出格式

        my_loging.addHandler(ch)#对接
        my_loging.addHandler(fh)


        if level == 'DEBUG':
            my_loging.debug(msg)
        elif level == 'INFO':
            my_loging.info(msg)
        elif level == 'WARNING':
            my_loging.warning(msg)
        elif level == 'ERROR':
            my_loging.error(msg)
        else:
            my_loging.critical(msg)

        my_loging.removeHandler(fh)#移除渠道
        my_loging.removeHandler(ch)

    def debug(self, msg):  # 简化
        self.loging_1('DEBUG',msg)

    def info(self, msg):
        self.loging_1('INFO',msg)

    def warning(self, msg):
        self.loging_1('WARNING', msg)

    def error(self, msg):
        self.loging_1('ERROR', msg)

    def critical(self, msg):
        self.loging_1('CRITICAL',msg)


if __name__ == '__main__':
    res=ReadLoging().info('7777')
    res2 = ReadLoging().info('77771')
    res3 = ReadLoging().info('77772')
    res4 = ReadLoging().info('77773')


















