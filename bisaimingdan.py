#!/usr/bin/python
#两个乒乓球队进行比赛，各出三人。
#甲队为a,b,c三人，乙队为x,y,z三人。
#已抽签决定比赛名单。有人向队员打听比赛的名单。
#a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

for a in ['x', 'y', 'z']:                               #a在xyz中挑一个打
    for b in ['x', 'y', 'z']:                           #b在xyz中挑一个打
        for c in ['x', 'y', 'z']:                       #c在xyz中挑一个打
            if a!=b and b!=c and c!=a:                  #a,b,c不能同时挑选同一个人
                if a!='x' and c!='x' and c!='z':        #依据题意不能ax，cx，cz
                    print('a'+a, 'b'+b, 'c'+c)

