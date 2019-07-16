# _*_ coding:utf-8 _*_
# @time     :  23:33
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : homework_2.py


# 2、一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，
# 会给10%的折扣，如果购买金额大于100元会给20%折扣。
# 编写一程序，询问购买价格，再显示出折扣（10%或20%）和最终价格 

money=float(input('你购买金额达到多少钱：'))#money代表总共购买的金额
if 50<= money <=100:
    f_money = money * 0.9#f_money代表最终价格
    print('你购买金额达到{}元，有10%的折扣，最终价格是{}'.format(money,f_money))
elif money > 100:
    f_money = money * 0.8
    print('你购买金额达到{}元，有20%的折扣，最终价格是{}'.format(money, f_money))
elif money < 50:
    f_money = money
    print('你购买的金额为{}元,没有折扣，最终金额为{}'.format(money,f_money))