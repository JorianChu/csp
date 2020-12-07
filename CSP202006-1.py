#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/8/1  8:52
"""

n,m = map(int,input().split())
points = []

for i in range(n):
    x,y,class_point = input().split()
    x,y = int(x),int(y)
    point = [x,y,class_point]
    points.append(point)

for j in range(m):
    theta_0,theta_1,theta_2 = map(int,input().split())
    flag = 1
    class_positive = -1
    class_negative = -1
    for k in range(n):
        temp = theta_0+theta_1*points[k][0]+theta_2*points[k][1]
        # 对于每一个分类器，只会初始化一次
        if temp>=0:
            if class_positive == -1:
                class_positive = points[k][2]
                class_negative = 'B' if points[k][2] == 'A' else 'A'
            if points[k][2] != class_positive:
                print("No")
                flag = 0
                break
        else:
            if class_negative == -1:
                class_negative = points[k][2]
                class_positive = 'B' if points[k][2] == 'A' else 'A'
            if points[k][2] != class_negative:
                print("No")
                flag = 0
                break
    if flag:
        print("Yes")

'''
9 3
1 1 A
1 0 A
1 -1 A
2 2 B
2 3 B
0 1 A
3 1 B
1 3 B
2 0 A
0 2 -3
-3 0 2
-3 1 1
'''