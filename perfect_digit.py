#!/usr/bin/python
#一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
for num in range(1,1001):
    arr = []
    for i in range(1,num):
        if num%i==0:
            arr.append(i)
    if sum(arr)==num:
        print(num,arr)
