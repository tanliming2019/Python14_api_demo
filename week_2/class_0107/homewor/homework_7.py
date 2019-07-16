# _*_ coding:utf-8 _*_
# @time     :  1:21
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : homework_7.py
# d1={1:'平价菜',2:'凉菜',3:'小锅现炒'}
# # a2='平价菜'
# # b2='凉菜'
# # c2='小锅现炒'
# d2={'手撕包菜':'10元','大白菜':'10元','凉拌黄瓜':'8元','凉拌皮蛋':'8元','大盘花菜':'16元'}
# A=str(input('输入菜单:'))
# if A in d1:
#     B=str(input('输入菜式:'))
#     if B in d2:
#         print(d[b])

# A='平价菜'
# B='凉菜'
# C='小锅现炒'
# d1={'手撕包菜':'10元','大白菜':'10元','土豆丝':'10元','炒莴笋':'10元','上海青':'10元','青椒炒茄子':'10元',
#     '焖白豆腐':'10元','青椒香干':'10元','茄子肉沫':'11元','茄子豆角':'11元','西红柿炒蛋':'12元'}
# d2={'凉拌黄瓜':'8元','凉拌皮蛋':'8元'}
# d3={'水煮鸡':'26元','大盘花菜':'16元','红烧鱼块':'18元','长豆角鲮鱼':'19元',
#     '水煮鱼（小）':'15元','水煮鱼（大）':'27元'}
# D=str(input('输入菜单：'))
# E=str(input('输入菜式：'))
# if D in A and E in d1:
#     print(E+d1[E])
# elif D in B and E in d2:
#     print(E+d2[E])
# elif D in C and E in d3:
#     print(E+d3[E])
# else:
#     print('不存在这道菜')

dishes={'平价菜':{'手撕包菜':10,'大白菜':10},
        '凉菜':{'凉拌黄瓜':8,'凉拌皮蛋':8},
      '小锅现炒':{'水煮鸡':26,'大盘花菜':16}}
d_type=input('请输入菜品类目：')
if d_type in dishes.keys():
    d_name= input('请输入菜名：')
    if d_name in dishes[d_type].keys():
        print('你选择的菜名是{},价格是{}'.format(d_name,dishes[d_type][d_name]))
    else:
        print('你输入的菜名不存在！')
else:
    print('你输入的菜品类目不存在')



