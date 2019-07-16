# _*_ coding:utf-8 _*_
# @time     :  0:05
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : learm_pandas.py
import pandas as pd
df=pd.read_excel('python14.xlsx')
print(df.loc[[1,2,3]].values)
print(df.index.values)