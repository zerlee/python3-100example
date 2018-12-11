#!/usr/bin/python
#对10个数进行排序

#冒泡排序
a = [1,5,7,3,2,4,9,10,6,8]
b = [a[0]]
for num in a[1:]:
    for i in range(len(b)):
        if num<b[i]:
            b.insert(i,num)
            break
    else:
        b.append(num)
print(b)
