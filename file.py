#!/usr/bin/python
#从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个’#为止



path='/root/file.txt'

while True:
    str = input()
    if str == '#':
        break
    else:
        with open(path,'a+') as f:
            f.write(str)
