# _*_ coding:utf-8 _*_
# @time     :  22:31
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : homework_2.py

# 2：编写一个类：你们自行去设计，要求写一个类，
# 初始化函数 、对象函数、 包含 根据你不同的选择完成get请求 OR post请求 ，
# 其中url 需要做参数化，并且最后要拿到响应结果
import requests
class Req:
    '''这是一个请求类'''
    def __init__(self,url1,url2):#初始化函数
        self.url1=url1
        self.url2=url2
    #get请求函数
    def Get_req(self):
        res_1=requests.get(self.url1)
        return print(res_1.text)#返回响应结果

    #post请求函数
    def Post_req(self):
        res_2=requests.post(self.url2)
        return print(res_2.text)


if __name__ == '__main__':
    P=Req('https://123.sogou.com/','https://www.sina.com.cn/')#创建一个对象
    P.Get_req()
    P.Post_req()



