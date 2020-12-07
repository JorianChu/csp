#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/11/26  15:48
"""


arr = list(map(int,input().split()))
n = len(arr)
# i,score = 0,0
score = 0
add_score = 2
for item in arr:
    if item==1:
        score += 1
        add_score = 2
    elif item==2:
        score += add_score
        add_score += 2
print(score)