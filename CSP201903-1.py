#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/7/6  11:01
"""

n = int(input())
num_l = sorted(list(map(int,input().split())))
m = n//2
if n-m*2:
    median = num_l[m]
else:
    # 注意这里的结果是浮点数
    median = (num_l[m-1]+num_l[m])/2
    if median!=int(median):
        median = round(median,1)
    else:
        median = int(median)
print(' '.join(map(str,[num_l[-1],median,num_l[0]])))



