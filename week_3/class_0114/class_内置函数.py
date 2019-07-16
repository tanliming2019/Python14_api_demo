# _*_ coding:utf-8 _*_
# @time     :  22:18
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : class_内置函数.py


# s='人生苦短，我用Python!'


# print(s[0:6:1])
#
# s[0]='commeng'
# print(s)
#
# print(id(s))
#
# s=s+'4444'
# print(s)
# print(id(s))

# s.format('发年终奖了吗')

def add(*args):
    print('arg的参数类型是',args)

    sum=0
    for item in args:
        print('参数值是',item)

        sum+=item
    print('求和的值',sum)
add(1,2,3)
#
# a=[1,2,3]
#
# add(*a)


#
# def call_person(**kwargs):
#     print(kwargs)
#
# call_person(name='华华',msg='来吃饭')

# s='人生苦短，我用PYTHON!'

# # res=s.format('发年终奖了没')
# # #
# # # print(res)
# #
# # print(s.capitalize())

#
print(s.find('Python'))
#
# print(s.join ('1234'))
#
# print(s.lower())

# # print(s.replace('P','@',1))
# s='hello python'
#
# # print(s.split('l',1))
#
# # print(s.strip('h'))
#
# # print(s.swapcase())
#
# print(s.index('l'))