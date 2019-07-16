# _*_ coding:utf-8 _*_
# @time     :  23:32
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : logging模块.py

import logging
#1、定义一个日志收集器，还要设置级别  getlogger
my_longger=logging.getLogger('python14')
my_longger.setLevel('ERROR')

#2、指定输出渠道，还要设置级别  streamHandler----控制台   FileHandler---指定文件
formatter=logging.Formatter('[%(asctime)s]-[%(levelname)s]-[日志信息:%(message)s]')
ch=logging.StreamHandler()
ch.setLevel('ERROR')
ch.setFormatter(formatter)

fh=logging.FileHandler('test1.log',encoding='utf-8')
fh.setLevel('INFO')


#3、对接  最终信息取两者的交集
my_longger.addHandler(ch)   #日志收集器收集到的信息输入到ch渠道            
my_longger.addHandler(fh)


my_longger.debug('This is debug msf')
my_longger.info('我是Python14期的老师，华华')
my_longger.warning('This is warning msg')
my_longger.error('我今天缺课了')
my_longger.critical('This is critical msg')


my_longger.removeFilter(fh)
my_longger.removeFilter(ch)   #用完一定要记得移除渠道，不然日志会有很多重复的信息


#
# logging.debug('This is debug msf')
# logging.info('我是Python14期的老师，华华')
# logging.warning('This is warning msg')
# logging.error('我今天缺课了')
# logging.critical('This is critical msg')                    