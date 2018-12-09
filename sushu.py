#!/usr/bin/python
#判断101-200之间有多少个素数，并输出所有素数。
arr = [2,3]
for i in range(4,201):
    for j in arr:
        if i%j==0:
            break
    else:
        arr.append(i)
for i in range(len(arr)):
    if arr[i]>100:
        l = arr[i:]
        print(len(l),l)
        break
