#!/usr/bin/python
#写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n

#n =17
#ls =sum([1/i for i in range(n,0,-2)])
#print(ls)


def f(n):

    if n%2==0:
        sum1=0
        for i in range(2,n+1,2):
            sum1 +=1/i
        print(sum1)
    
    elif n%2==1:
        sum2=0
        for i in range(1,n+1,2):
            sum2 +=1/i
        print(sum2)

if __name__=='__main__':
    n=int(input())
    f(n)
