#!/usr/bin/python
#求1+2!+3!+...+20!的和
s, t = 0, 1
for n in range(1,20):
    t*=n
    s+=t
print(s)
