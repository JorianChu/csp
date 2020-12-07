#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/11/26  15:47
"""

n = int(input())
dic = {1:0,2:0,3:0,0:0}
i = 1
count = 0
while(count != n):
    if i % 7 == 0 or '7' in str(i):
        dic[i%4] += 1
    else:
        count += 1
    i += 1
for i in dic.values():
    print(i)