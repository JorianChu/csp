#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/8/1  10:04
"""

n = int(input())

# dic = {}
list_l = []
for i in range(n):
    x, y = map(int, input().split())
    list_l.append((x,y))
    # dic[(x,y)] = 1

cnt = [0,0,0,0,0]
for item in list_l:
    x,y = item[0],item[1]
    if (x, y - 1) in list_l and (x, y + 1) in list_l and (x - 1, y) in list_l and (x + 1, y) in list_l:
        lis_temp = []
        lis_temp.append((x-1,y-1))
        lis_temp.append((x-1,y+1))
        lis_temp.append((x+1,y-1))
        lis_temp.append((x+1,y+1))

        num = 0
        for tuple_t in lis_temp:
            if tuple_t in list_l:
                num += 1
        cnt[num] += 1

# for key,value in dic.items():
#     x = key[0]
#     y = key[1]
#     if dic[(x,y-1)] and dic[(x,y+1)] and dic[(x-1,y)] and dic[(x+1,y)]:
#         cnt[dic[(x-1,y-1)] + dic[(x-1,y+1)] + dic[(x+1,y-1)] + dic[(x+1,y+1)]] += 1

for i in range(5):
    print(cnt[i])

'''
7
1 2
2 1
0 0
1 1
1 0
2 0
0 1

11
9 10
10 10
11 10
12 10
13 10
11 9
11 8
12 9
10 9
10 11
12 11
'''
