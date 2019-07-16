# _*_ coding:utf-8 _*_
# @time     :  0:27
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : class_条件语句.py
#
# sex=input('请输入你的性别：')
# if sex == '女':
#     print('和华华老师一起shopping吧')



# task_score=int(input('请输入你的分数:'))
# absence=int(input('请输入你的缺勤次数:'))
# if task_score == 100 and absence == 0 :
#     print('恭喜你，荣获班级之星')
# else:
#     print('你的分数是{},缺勤次数是{}次，离班级之星还有一定的距离'.format(task_score,absence))

#
# s=(1)
# if s:
#     print('我喜欢花呗')
# else:
#     print('我不喜欢花呗')

# name= input('请输入你的名字：')
# height= int(input('请输入你的身高：'))
# if name == '马云':
#     print('这样的对象挺好的')
# elif name!='马云':
#     if height== 180:
#         print('这样的对象挺好的')
#     else:
#         print('没啥好说的')
#
# color=input('请输入你看到的灯的颜色：')
# if color=='red':
#     print('请不要乱动，现在是红灯，有危险！')
# elif color=='yellow':
#     print('请耐心等候，现在是黄灯，不要乱闯黄灯！')
# elif color=='green':
#     print('请注意过往车辆，现在可以安全通行')
# else:
#     print('这个颜色不对，你是不是色盲！')

#
#
# d={'name':'huahua','pwd':'123456'}
# s1=input('请输入用户名：')
# s2=input('请输入密码：')
# if s1==d['name']and s2==['pwd']:
#     print('登录成功')
# elif s1=='huahua'or s2=='123456':
#     print('用户名或密码错误')
# else:
#     print('用户名和密码都错误')



d={'vampire':'123456','nancy':'666666'}

s=input('请输入你的用户名：')
if s in d.keys():
    pwd=input('请输入你的密码：')
    if pwd ==d[s]:
        print('登录成功')
    else:
        print('密码错误')
else:
    print('用户名错误')