#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/11/28  17:34
"""

n,X,Y = list(map(int,input().split()))
dic = {}
for i in range(1,n+1):
    x_temp,y_temp = list(map(int,input().split()))
    dis = (X-x_temp)*(X-x_temp) + (Y-y_temp)*(Y-y_temp)
    dic[i] = dis

sorted_lis = sorted(dic.items(), key=lambda x:x[1])
print("{}\n{}\n{}".format(sorted_lis[0][0],sorted_lis[1][0],sorted_lis[2][0]))