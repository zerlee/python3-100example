#!/usr/bin/python
#题目004：输入某年某月某日，判断这一天是这一年的第几天

#考察时间元组的概念属性和time模块方法的熟练程度

import time
date=  input('输入时间(例如2018-01-23)：')
st  = time.strptime(date,"%Y-%m-%d")  #根据fmt的格式把时间字符串解析为时间元组
num = st.tm_yday
print(num)
