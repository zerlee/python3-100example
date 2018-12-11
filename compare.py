#!/usr/bin/python
arr=[]
for i in range(3):
    a = int(input('请输入数字'))
    arr.append(a)
arr.sort(reverse=True)
print('从大到小',arr)

