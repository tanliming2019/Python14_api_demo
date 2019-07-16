# _*_ coding:utf-8 _*_
# @time     :  19:48
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : do_mysql.py

import pymysql
from API_5.common.read_config import ReadConfig
from API_5.common import project_path

class DoMySql:
    '''这是一个操作数据库的类，专门进行数据的读取'''
    def do_mysql(self,query,flag=1):
        '''
        ：query表示sql查询语句
        :flag 标志1 获取一条数据  2获取多条数据'''
        db_config=ReadConfig(project_path.conf_path).get_data('DB','db_config')
        cnn=pymysql.connect(**db_config)#建立一个连接

        cursor=cnn.cursor()#获取游标，获取操作数据库的权限

        cursor.execute(query)#执行查询语句

        if flag==1:
            res=cursor.fetchone()#获取查询结果并且打印结果
        else:
            res=cursor.fetchall()
        return res


if __name__ == '__main__':
    query='select Id from loan where MemberID = 115'
    res=DoMySql().do_mysql(query,1)
    print(res)
    print(type(res))
