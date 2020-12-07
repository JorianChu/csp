#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/8/15  17:35
"""

w = int(input())
k = ""
num = 0
count = 0
ans = []
flag1,flag2 = 0,0
for _ in range(w):
    line = input()
    # if line.strip() == '':
    #     pass
    line = line.strip()
    if line.strip() == '':
        flag1 = 2
        continue
    if flag1==2:
        count+=1
    count += 1

print(count)
    # num = len(line)
    # while(line):
    #     if num==w:
    #         ans[count] += k
    #         count += 1
    #         k = ""
    #         num = 0
    #     line = line[k]

