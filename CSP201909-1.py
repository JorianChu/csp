#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/7/6  9:08
"""

N,M = map(int,input().split())

T = 0
k_l = []

for i in range(N):
    temp_l = list(map(int, input().split()))
    # temp = -sum(temp_l[1:])
    # for j in range(1,M+1):
    #     temp
    k_l.append(-sum(temp_l[1:]))
    T = T + temp_l[0] - k_l[i]

index = k_l.index(max(k_l))
num = k_l[index]
print(T,index+1,num)