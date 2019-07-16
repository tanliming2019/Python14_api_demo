# _*_ coding:utf-8 _*_
# @time     :  22:05
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : class_异常处理.py

# a=10
# try:
#     print(a)
# except:
#     print('try里面的代码出错了')

# try:
#     print(a)
# except Exception as e:#捕抓错误
#     print('try里面的代码出错：{}'.format(e))




# file=open('log.txt','a+',encoding='utf-8')
# b=[1,2,3,4,5]
# try:
#     print(b[9])
# except IndexError as e:
#     print('try里面的代码出错：{}'.format(e))
#     file.write(str(e))
#     file.write('\n')
#     file.close()


#
# try:
#     file=open('test.txt',encoding='utf-8')#默认只读r
#     file.write('我是python14的华华')
# except Exception as e:
#     print('try里面的代码报错：{}'.format(e))
# finally:
#     file.close()
# print(file.closed)



# try:
#     a='wo'
#     b=2
#     print(a+b)
# except Exception as e:
#     print('try里面的代码报错：{}'.format(e))
# else:
#     c=5
#     f=6
#     print(c+f)



with open('log.txt') as file:#打开log.txt 存到file里面
    res= file.read()
    print(res)
print(file.closed)