# _*_ coding:utf-8 _*_
# @time     :  22:38
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : learn_re.py



from API_6.common.get_data import GetData
import re

target="{'mobliephone':'#normal_user#','pwd':'#normal_pwd#'}"
p='normal_user'#原义字符查找
p2='#(.*?)#'

#
# m=re.search(p2,target)#在目标字符串里面根据正则表达式来查找，有匹配的字符串就返回对象
# print(m)
# print(m.group(1))


# mm=re.findall(p2,target)
# print(mm)
#
# target2=re.sub(p2,'15013131044',target,count=1)
# print(target2)

while re.search(p2,target):
    m=re.search(p2,target)#search是查找到一个就立刻返回一个match对象
    key=m.group(1)
    value=getattr(GetData,key)
    target=re.sub(p2,value,target,count=1)#替换后重新赋值
    print(target)