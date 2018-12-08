#!/usr/bin/python
#将一个列表的数据复制到另一个列表中
#Python里面一切都是对象，list的复制需要用[:]的方式。
#至于b=a只是相当于给a取了个别名而已，指向的是同一个列表，并没有实现复制。
a = [1,2,3]
b = a[:]

'''拓展'''
a[0]=0
print(id(a),id(b)) #查看a，b的内存地址
print(a,b)

#a=[1,2,3]
#b=a
#a[0]=0
#print(id(a),id(b))
#print(a,b)
#
#
