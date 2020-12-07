#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/11/26  15:20
"""
n = int(input())
# arr = []
arr = list(map(int,input().split()))

arr_new = sorted(arr)

min = arr_new[-1]
for i in range(len(arr_new)-1):
    temp = abs(arr_new[i+1]-arr_new[i])
    if temp < min:
        min = temp
print(min)