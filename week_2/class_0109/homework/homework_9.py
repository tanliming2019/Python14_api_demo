# _*_ coding:utf-8 _*_
# @time     :  23:15
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : homework_9.py


# 9:购物车程序 需求：
# 1：启动程序后，让用户在控制台输入工资，然后打印商品信息（随便你们自己用什么方式存储商品，记得要有商品的编号、名称以及价格） 
# 2：允许用户根据商品编号购买商品 
# 3：用户选择商品后，监测余额是否足够，如果足够就直接扣款，不够就提醒用户，不能购买这个商品。 
# 4：可随时退出，退出后，打印已购买商品和余额

dict_prod={'001':['豆沙包',2.5],'002':['奶黄包',3],'003':['菜包',1.5]}  #dict_prod商品信息
salary=input('请输入你的工资:')
print('你可以购买的商品有：{}'.format(dict_prod))#展示可购买的商品信息
prod_sum = 0  # 个人余额
prod_total = 0  # 购买商品总额

while True:
    prod_number=str(input('请输入你要购买的商品编号：'))
    if prod_number in dict_prod:
        prod_count = int(input('请输入你要购买的商品数量：'))
        prod_price=dict_prod[prod_number][1]#选择的商品的单价
        prod_name=dict_prod[prod_number][0]#选择的商品的名称

        if prod_total<=int(salary):
            prod_total=prod_price*prod_count
            prod_sum=int(salary)-prod_total
            print('已购买商品{}{}个，商品总金额为{}，个人余额为{}'.format(prod_name,prod_count,prod_total,prod_sum))
            continue
        else:
            print('余额不足，不能购买这个商品')
            break

    elif prod_number=='n':
        print('退出购买')
        break

    else:
        print('不存在这个商品')
        continue



