# _*_ coding:utf-8 _*_
# @time     :  22:43
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : class_where循环.py
# c=0
# while True:
#     print('hello，我是python')
#     c+=1
#     if c==10:
#         break

# c=0
# while c<10:
#     print('hello,我是python')
#     c+=1




c=0#询问次数
a=0#符合条件人数
while c<5:
    sex=str(input('请输入性别：'))
    age=int(input('请输入年龄：'))

    if sex=='f' and 10<=age<=12:
        print('符合加入条件')
        a+=1
    else:
        print('不符合加入条件')
    c+=1
print(a)
