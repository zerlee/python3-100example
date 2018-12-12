#!/usr/bin/python
#入一个奇数，然后判断最少几个 9 除于该数的结果为整数

x = int(input('输入一个奇数:'))
for i in range(1,61):
    if int('9'*i)%x==0:
        print(i)
        break
else:
    print('no way')
