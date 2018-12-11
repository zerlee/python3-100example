#!/usr/bin/python
# 求100之内的素数
arr = [2]
for i in range(3, 101):
    for j in arr:
        if i%j==0:
            break
    else:
        arr.append(i)
print(arr)
