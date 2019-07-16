# _*_ coding:utf-8 _*_
# @time     :  19:35
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : http_request.py

import requests
class HttpRequest:
    '''该类完成get以及post请求，并返回结果'''
    def http_request(self,method,url,param,cookies):
        '''根据请求方法来决定发起get请求还是post请求
        methond:get  post   http的请求方式
        url:发送请求的接口地址
        param:随接口发送的请求参数  以字典的格式传递
        resp:有返回值，返回结果是响应报文
        '''
        if method.upper()=='GET':
            try:
                resp=requests.get(url,params=param,cookies=cookies)
            except Exception as e:
                print('get请求方式出错了：{}'.format(e))

        elif method.upper()=='POST':
            try:
                resp=requests.post(url,data=param,cookies=cookies)
            except Exception as e:
                print('post请求方式出错了：{}'.format(e))

        else:
            print('不支持该种请求方式')
            resp=None

        return resp

if __name__ == '__main__':
    url='http://test.lemonban.com/futureloan/mvc/api/member/register'
    param={'mobilephone':'15013131020','pwd':'a12345678','regname':'Ming'}
    method='get'
    resp=HttpRequest().http_request(method,url,param)
    print(resp.text)
