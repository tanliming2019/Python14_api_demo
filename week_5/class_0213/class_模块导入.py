# _*_ coding:utf-8 _*_
# @time     :  22:29
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : class_模块导入.py

#
# def add(a,b):
#     print(a+b)
#
# add(1,2)
# add(10,20)


# import week_5.class_0213.add
# res=week_5.class_0213.add.add(10,3)
# print(res)
#
# import week_5.class_0213.add as t
# res=t.add(10,38)
# print(res)



from week_5.class_0213.add import add_1
res=add_1(5,6)
print(res)


from week_5.class_0213 import add
res=add.add_1(5,6)
print(res)



