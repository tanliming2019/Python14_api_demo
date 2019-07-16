# _*_ coding:utf-8 _*_
# @time     :  22:55
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : homework_进阶1.py
#
# 进阶2：搜索引擎中会对用户输入的数据进行处理，
# 第一步就是词法分析，分离字符串中的数字、中文、拼音、符号。
# 比如这个字符串： 我的是名字是lemon,今年5岁。 语法分析后得到结果如下： 
# 数字：5 
# 中文：我的名字是、今年、岁 
# 拼音：lemon
# 符号：，。 请编写程序实现该词法分析功能。 

def data_treating(x0):
    y=j=z=h=''
    for x1 in x0:
        if x1.isdigit():#判断是否是数字
            y=y+x1
        elif x1 >= u'\u4e00' and x1 <= u'\u9fa5':#判断是否是中文
            j=j+x1
        elif x1.isalpha():#判断是否是拼音
            z=z+x1
        else:#判断是否是符号
            h=h+x1

    print('''    数字：{}
    中文：{}
    拼音：{}
    符号：{}'''.format(y,j,z,h))

data_treating('我的是名字是lemon,今年5岁。')


