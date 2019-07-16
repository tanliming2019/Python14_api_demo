# _*_ coding:utf-8 _*_
# @time     :  2:11
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : learn_requests.py

import requests
# #注册请求
# url='http://test.lemonban.com/futureloan/mvc/api/member/register'
# param={'mobilephone':'15013131042','pwd':'a12345678','regname':'lemonMing'}
#
# # #发送一个get请求
# # resp=requests.get(url,params=param)#返回一个消息实体
# # print(type(resp.text))#字符串
# # print(resp.text)
# # print(type(resp.json()))#字典
# # print(resp.json())
#
# #发送一个post请求
# resp=requests.post(url,data=param)#返回一个消息实体
# print(type(resp.text))#字符串
# print(resp.text)
#
# print(type(resp.json()))#字典
# print(resp.json())


# #===登录请求====
# url='http://test.lemonban.com/futureloan/mvc/api/member/login'
# param={'mobilephone':'15013131042','pwd':'a12345678'}
#
# #发送一个get请求
# resp=requests.get(url,params=param)#返回一个消息实体
# print(type(resp.text))#字符串
# print(resp.text)
# print(type(resp.json()))#字典
# print(resp.json())
# #
# # #发送一个post请求
# # resp=requests.post(url,data=param)#返回一个消息实体
# # print(type(resp.text))#字符串
# # print(resp.text)
# #
# # print(type(resp.json()))#字典
# # print(resp.json())


import json
# s='{"status":1,"code":"10001","data":null,"msg":"登录成功"}'
# # value=json.loads(s)
# # print(value)

s={'status': 1, 'code': '10001', 'data': None, 'msg': '登录成功'}
value=json.dumps(s,ensure_ascii=False)
print(value)