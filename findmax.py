#!/usr/bin/python
#找到年龄最大的人，并输出。

person = {"li":18,"wang":50,"zhang":20,"sun":22}

a = person.values() #将字典中的值取出来
list1 = list(person.values()) #将a变成列表
list1.sort() #对list1进行排序
print('年龄最大的人是: %s' % list1[-1]) #输出列表中最大的值

