#!/usr/bin/python
#请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

def juge(num,week_list):
    w=input('请输入第%s字母:' %num)
    w=w.lower()
    res = []
    state = 0
    for week in week_list:
        if w == week[0+num-1:1+num-1]:
            state +=1
            res.append(week)

    if state ==1:
        print(res[0])
    elif state >1:
        num = num +1
        week_list=res
        juge(num,week_list)
    else:
        print('你的输入不正确，请重新输入')

if __name__=='__main__':
    num =1
    week_list = ['monday', 'tuseday','wednesday','thursday','friday','saturday','sunday']
    juge(num,week_list)



