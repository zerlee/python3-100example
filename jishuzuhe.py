#!/usr/bin/python
#求0—7所能组成的奇数个数

#计算出组成数字的个数，再用set去重,再用x%2==1过滤出奇数

s= [i for i in '01234567']
import itertools
arr = []  #数字总个数
for i in range(1,9):
    a = list(itertools.permutations(s,i))
    l = list(map(lambda x:int(''.join(x)),a))
    arr+=l
    print(i,len(l))    #输出组成的数字，不同位数的都有多少
arr1 = set(arr) #去重
arr2 = list(filter(lambda x:x%2==1,arr1)) #过滤奇数
print(len(arr),len(arr1),len(arr2))
