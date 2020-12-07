#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/8/15  15:18
"""

n = int(input())
S = input()

init_s = '1'
for _ in range(n):
    temp_str = ''
    for c in init_s:
        temp_str += str(1<<int(c))
    init_s = temp_str

print(init_s.count(S))