#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/6/29  9:11
"""
# list_l = list(map(int,input().split()))
# n,m = list_l[0],list_l[1]
n,m = map(int,input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int,input().split())))
for j in range(m):
    for k in range(n):
        print(matrix[k][m-j-1],end=' ')
    print()