#!/usr/bin/pyhon
#输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组
a = [6,3,10,2,5,1,4,7,9,8]
i = a.index(max(a))
a[0],a[i] = a[i],a[0]
i = a.index(min(a))
a[-1],a[i] = a[i],a[-1]
print(a)
