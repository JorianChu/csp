#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/12/7  17:26
"""

n,k = map(int,input().split())
lis = [1]*(n+1)
i,num,now = 0,1,1
while i<n-1:
    now += 1
    if now>n:
        now = 1
    if lis[now]==0:

        continue
    if num%k==0 or str(num)[-1]==k:
        lis[now] = 0
        i += 1
    num += 1

for i in range(1,len(lis)+1):
    if lis[i]:
        print(i)

# for i in range(n):
#     if lis[i]==0:
#         continue
#     if i%k==0 or str(i)[-1]==k:
#         lis[i] = 0


# dic = {1:1}
# print(type(dic.keys()))
#
# print(list(dic.keys())[0])