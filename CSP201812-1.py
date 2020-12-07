#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/7/6  16:48
"""
# 这里是到达路口时，看到的各交通灯的倒计时
r,y,g = map(int,input().split())
n = int(input())
sum = 0
for i in range(n):
    k,t = map(int,input().split())
    if k==0 or k==1:
        sum += t
    elif k==2:
        sum += t+r
print(sum)