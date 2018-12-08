#!/usr/bin/python

for i in range(1,10): #依次将1-9赋值给i
    for  j in range(1,i+1): #当i为1时，j为1,当i为2时，j为1,2,当i为3时，j为1,2,3...
        string = '%d*%d=%d'%(j,i,j*i)        
        print('%-7s'%string,end='') #-7s将等式长度固定为7个字符，循环内的等式不换行
    print('') #换行
