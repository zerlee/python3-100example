#!/usr/bin/python
#一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同
#num = int(input())
#list1=list(str(num))
#
#if list1[0] == list1[4] and list1[1]== list1[3]:
#    print('yes')
#else:
#    print('no') 

num = int(input())
s = str(num)
for i in range(len(s)//2):
    if s[i] == s[-i-1]:
        print(True)
        break
else:
    print(False)
