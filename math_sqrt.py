#!/usr/bin/python
#题目003：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

import math
for i in range(1000):
    x = math.sqrt(i+100)
    y = math.sqrt(i+100+168)
    if x%1==0 and y%1==0:
        print(i)
