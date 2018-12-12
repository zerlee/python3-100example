#!/usr/bin/python
#从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存

str1 = input()

str1 = str1.upper()

with open('/root/test','w+') as f:f.write(str1)
