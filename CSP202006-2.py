#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/8/1  9:37
"""

n,a,b = map(int,input().split())

dic = {}
ans = 0
for i in range(a):
    index, value = [int(x) for x in input().split(' ')]

    dic[index] = value

for j in range(b):
    index, value = [int(x) for x in input().split(' ')]
    if index in dic.keys():
        ans += dic[index]*value
print(ans)

# ans = 0
# i = j = 0
# while i<a and j<b:
#     if vector1[i][0]==vector2[j][0]:
#         ans += vector1[i][1]*vector2[j][1]
#         i += 1
#         j += 1
#     elif vector1[i][0]<vector2[j][0]:
#         i += 1
#     else:
#         j += 1
# print(ans)

'''
10 3 4
4 5
7 -3
10 1
1 10
4 20
5 30
7 40
'''