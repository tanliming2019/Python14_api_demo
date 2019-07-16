# _*_ coding:utf-8 _*_
# @time     :  0:56
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : http_request.py

import requests
res=requests.get('http://www.baidu.com')
print(res.text)

res_1=requests.post('http://www.baidu.com')

print(res_1)