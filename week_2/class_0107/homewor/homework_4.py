# _*_ coding:utf-8 _*_
# @time     :  0:00
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : homework_4.py

# 4、输入一个年份，输出是否为闰年，闰年条件：能被4整除但不能被100整除，或者能被400整除的年份都是闰年 
year=int(input('请输入一个年份：'))
if year %4==0 and year %100!=0:
    print('{}年为闰年'.format(year))
elif year %400==0:
    print('{}年为世纪闰年'.format(year))
else:
    print('{}年不是闰年'.format(year))


