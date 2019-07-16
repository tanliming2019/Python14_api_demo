# _*_ coding:utf-8 _*_
# @time     :  15:55
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : learn_mysql.py
import pymysql
#第一步：连接数据库
#提供数据库的连接信息
db_config={'host':'test.lemonban.com',
           'user':'test',
           'password':'test',
           'port':3306,
           'database':'future'
           }
cnn=pymysql.connect(**db_config)#建立一个连接

#第二步：获取游标，获取操作数据库的权限
cursor=cnn.cursor()

#第三步：操作数据库表
query='select MobilePhone from member where Id < 1231'
cursor.execute(query)

#第四步：获取查询结果并且打印结果
res1=cursor.fetchone()
# res2=cursor.fetchall()

print('数据库的查询结果1:{}'.format(res1))
# print('数据库的查询结果1:{}'.format(res2))
