#!/usr/bin/python
#求输入数字的平方，如果平方运算后小于 50 则退出
num = int(input())
while num*num < 50:
    break
else:
    print(num*num)
