#!/usr/bin/python
#某个公司采用加密方式传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：
#每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位
#交换。编写加密的函数与解密的函数。 '''

#加密过程

def jiami(num):
    if num>1000 and num<9999:
        a = num//1000  #取出千位数
        a1 = (a+5)%10

        b = num//100%10
        b1 = (b+5)%10

        c = num//10%10
        c1 = (c+5)%10

        d=num%10
        d1 = (d+5)%10
        print(d1*1000+c1*100+b1*10+a1)


jiami(1235)
