#!/usr/bin/python
#author:hanli
#有四个数字：1,2,3,4能组成多少个互不相同且无重复数字的三位数

arr = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            num = 100*i + 10*j + k
            if i!=k and j!=k and i!=j and num not in arr:
                arr.append(num)
print("一共可以组成%s个数字,分别是%s" % (len(arr),arr))
