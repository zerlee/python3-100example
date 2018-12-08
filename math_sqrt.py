#!/usr/bin/python
import math
for i in range(1000):
    x = math.sqrt(i+100)
    y = math.sqrt(i+100+168)
    if x%1==0 and y%1==0:
        print(i)
