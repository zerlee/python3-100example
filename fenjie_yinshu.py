#!/usr/bin/python
#将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
import math
num = int(input('输入一个整数:'))
arr = []
while num>1:
    for i in range(2, int(math.sqrt(num))+1):
        if num%i==0:
            arr.append(i)
            num = num//i
            break
    else:
        arr.append(num)
        break
print(arr)
