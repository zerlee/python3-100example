#!/usr/bin/python
#输入三个整数x,y,z，请把这三个数由小到大输出
print('输入三个数字')
x = input('输入第一个数字')
y = input('输入第二个数字')
z = input('输入第三个数字')
l = [x,y,z]
arr = sorted(l)
print(arr)
