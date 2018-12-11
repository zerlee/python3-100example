#!/usr/bin/python
#矩阵相加

x = [[12,7,3],[4,5,6],[7,8,9]]
y = [[5,8,1],[6,7,3],[4,5,9]]

z = y[:]
for i in range(3):
    for j in range(3):
        z[i][j]=x[i][j]+y[i][j]
print(z)
      
