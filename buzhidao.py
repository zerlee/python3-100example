#!/usr/bin/python
#809*??=800*??+9*?? 其中??代表的两位数, 
#809*??为四位数，8*??的结果为两位数，9*??的结果为3位数。
#求??代表的两位数，及809*??后的结果。

l = lambda x:len(str(x))

for i in range(10,100):
    if l(809*i)==4 and l(8*i)==2 and l(9*i)==3:
        x = i
        print(x)
