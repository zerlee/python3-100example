#!/usr/bin/python
#变量作用域， python是有分局部变量、全局变量的等区分的。
num = 2
def autofunc():
    num = 1
    print('internal num = %d' % num)
    num +=1

for i in range(3):
    print('The num = %d' % num)
    num +=1
    autofunc()
