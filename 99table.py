#!/usr/bin/python

for i in range(1,10): #依次将1-9赋值给i
    for  j in range(1,i+1): #当i为1时，j为1,当i为2时，j为1,2,当i为3时，j为1,2,3...
        print('%d*%d=%d'%(j,i,j*i),end=' ') #每输出一个等式后面加一个空格，将两个等式隔开
    print('') #换行
