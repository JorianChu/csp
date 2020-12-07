#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/7/2  15:55
"""

N = int(input())

maps = [[0]*100 for i in range(100)]
for i in range(N):
    retangle_l = list(map(int,input().split()))
    x1,y1,x2,y2 = retangle_l[0],retangle_l[1],retangle_l[2],retangle_l[3]
    for j in range(x1,x2):
        for k in range(y1,y2):
            maps[j][k] = 1

num = sum(map(sum,maps))
print(num)


