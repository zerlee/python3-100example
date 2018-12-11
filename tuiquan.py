#!/usr/bin/python
#有n个人围成一圈，顺序排号。
#从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位
#抽象为排队进门问题

n=5 #初始化n=34
arr = list(range(1,n+1)) #所有人门外站成一队a,进门的人进入队列b
count,a,b=0,arr,[] #计数器,还没开始报数进门的队列a,进门后的人组成的新队列b

while len(a+b)>1: #循环到只剩一人
    num=a.pop(0) #排队进门,每进一人即a.pop(0)
    count+=1 #每进一人,记一次数
    if count%3!=0:
        b.append(num)
    if a==[]:
        a,b=b,[]
print(a[0])
