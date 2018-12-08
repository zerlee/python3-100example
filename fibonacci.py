#!/usr/bin/python
#斐波那契数列
def fibonacci_loop(n):
    list = []
    a, b = 0, 1
    while n > 0:
        list.append(b)
        a, b = b, a + b
        n -= 1
    return list
print(fibonacci_loop(20))
        
