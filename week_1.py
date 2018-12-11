#!/usr/bin/python
letter = input('请输入一个字母')
letter = letter.lower()
if letter not in ['m','w','f','t','s']:
    print('输入错误')
    
elif letter == 'm':
    print('星期一')
elif letter == 'w':
    print('星期三')
elif letter == 'f':
    print('星期五')
elif letter == 's':
    w = input('请输入第二个字母')
    w = w.lower()
    if w == 'a':
        print('星期六')
    elif w =='u':
        print('星期日')
elif letter == 't':
    w1 = input('请输入第二个字母')
    w1 = w1.lower()
    if w1 == 'h':
        print('星期四')
    elif w1 =='u':
        print('星期二')
 
        
    
