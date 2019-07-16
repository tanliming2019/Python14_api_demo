# _*_ coding:utf-8 _*_
# @time     :  23:33
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : homework_1.py

# 1.根据你输入的数据，来进行判断学生的成绩。输入数据函数：input() 

grades=input('请输入你的成绩：')
if grades!='':
    if grades.isdigit():

        grades=float(grades)
        if grades >=0 and grades<=100:
            if grades >= 90:
                print('成绩等级：优秀')
            elif grades >= 80:
                print('成绩等级：优良')
            elif grades >= 60:
                print('成绩等级：及格')
            elif grades < 60 :
                print('成绩等级：不及格')
        else:
            print('你输入的分数超过0~100')
    else:
        print('请输入输入数字')
else:
    print('成绩输入不能为空')