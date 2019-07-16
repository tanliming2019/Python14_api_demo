# _*_ coding:utf-8 _*_
# @time     :  23:15
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : my_log.py

import logging
from week_7.class_0227.read_config import ReadConfig

class MyLog:
    def __init__(self):
        self.logger_name=ReadConfig('log.conf').get_str('LOG','logger_name')#日志名字
        self.level=ReadConfig('log.conf').get_str('LOG','logger_level')

    def my_log(self,level,msg):
        my_logger=logging.getLogger(self.logger_name)#定义一个日志收集器
        my_logger.setLevel(self.level)#设置级别

        formatter=logging.Formatter('[%(asctime)s]-[%(levelname)s]-[日志信息:%(message)s]')#日志输入格式
        ch=logging.StreamHandler()#指定输出渠道 ---控制台
        ch.setLevel(self.level)#设置级别
        ch.setFormatter(formatter)#设置日志输出格式

        formatter = logging.Formatter('[%(asctime)s]-[%(levelname)s]-[日志信息:%(message)s]')
        fh=logging.FileHandler('test1.log',encoding='utf-8')  #指定输出渠道 ---文件
        fh.setLevel(level)
        fh.setFormatter(formatter)


        #3、对接  最终信息取两者的交集
        my_logger.addHandler(ch)   #日志收集器收集到的信息输入到ch渠道
        my_logger.addHandler(fh)

        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        else:
            my_logger.critical(msg)

        my_logger.removeHandler(fh)  # fh ch
        my_logger.removeHandler(ch)  #一定要记得移除掉#用完一定要记得移除渠道，不然日志会有很多重复的信息

    def debug(self,msg):#简化
        self.my_log('DEBUG',msg)

    def info(self,msg):
        self.my_log('INFO',msg)

    def warning(self,msg):
        self.my_log('WARNING',msg)

    def error(self,msg):
        self.my_log('ERROR',msg)

    def critical(self,msg):
        self.my_log('CRITICAL',msg)




if __name__ == '__main__':


    P=MyLog()
    P.my_log('ERROR','发生错误')
    P.critical('1111')
