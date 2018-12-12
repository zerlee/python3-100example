#!/usr/bin/python
#列表转换为字典
l = ['ak17','b51','b52','#63']
d = {}

for i in range(len(l)):
    d[str(i)]=l[i]
print(d)
