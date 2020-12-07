#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/6/29  9:51
"""
n = int(input())
record = list(map(int,input().split()))
record_new = [1]*n
for i in range(n):
    for j in range(i+1,n):
        if a[j] == a[i]:
            record_new += 1
for item in record_new:
    print(item,end=" ")
