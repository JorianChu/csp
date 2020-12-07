#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/11/29  23:14
"""

n,m=map(int,input().split())
a=[]
flag=[0]*m
for i in range(n):
    a.append(list(input().split()))
for i in range(m):
    b0,b1,b2=map(int,input().split())
    for j in a:
        if b0+b1*int(j[0])+b2*int(j[1])<0:
            j.append('A')
        else:
            j.append('B')
        if j[-1]==j[2]:
            flag[i]=0
        else:
            flag[i]=1
            break
for i in range(m):
    if flag[i]==0:
        print('Yes')
    else:
        print('No')
