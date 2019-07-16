# _*_ coding:utf-8 _*_
# @time     :  2:48
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : get_data.py
import re
from API_6.common import read_config
from API_6.common import project_path

config=read_config.ReadConfig(project_path.conf_path)
print(config)
class GetData:
    '''该类可以用来动态地更改、删除、获取数据'''
    COOKIE=None
    # LOAN_ID=None #新添加的标ID  初始值

    normal_user=config.get_str('data','normal_user')
    normal_pwd=config.get_str('data','normal_pwd')
    normal_member_id=config.get_str('data','normal_member_id')

def replace(target):
    p2='#(.*?)#'
    while re.search(p2, target):
        m=re.search(p2, target)  # search是查找到一个就立刻返回一个match对象
        key=m.group(1)
        value=getattr(GetData, key)
        target=re.sub(p2, value, target, count=1)  # 替换后重新赋值
    return target









# print(getattr(GetData,'COOKIE'))
# print(hasattr(GetData,'COOKIE'))
# print(setattr(GetData,'COOKIE','123456'))
# print(getattr(GetData,'COOKIE'))
# print(delattr(GetData,'COOKIE'))
# print(getattr(GetData,'COOKIE'))
