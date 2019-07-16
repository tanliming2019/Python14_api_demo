# _*_ coding:utf-8 _*_
# @time     :  21:03
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : learm_requests_2.py

import requests

url='http://test.lemonban.com/futureloan/mvc/api/member/login'
param={'mobilephone':'15013131042','pwd':'a12345678','regname':'lemonMing'}

headers = {'user-agent': 'Mozilla/5.0'}
resp=requests.get(url,params=param,headers=headers)#返回一个消息实体

#
# print('状态码：',resp.status_code)
# print('响应头：',resp.headers)
# # print('请求报文：',resp.text)
# print('cookies:',resp.cookies)
# print('请求头：',resp.request.headers)

#充值
url='http://test.lemonban.com/futureloan/mvc/api/member/recharge'
param={'mobilephone':'15013131042','amount':'10000'}

resp=requests.post(url,data=param,cookies=resp.cookies)#返回一个消息实体
print('充值结果：',resp.text)
