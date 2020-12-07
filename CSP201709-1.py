#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/11/26  14:58
"""
import math

# N,10, 3+1 5+2
# n<300 10

# 7x + 4y
def max_count(N):
    x2 = N // 50
    rest_money = N % 50
    x1 = rest_money // 30
    x0 = (N - 50*x2 - 30*x1) // 10
    print(7 * x2 + 4 * x1 + x0)

if __name__ == '__main__':
    N = int(input())
    x2 = N // 50
    rest_money = N % 50
    x1 = rest_money // 30
    x0 = (N - 50 * x2 - 30 * x1) // 10
    print(7 * x2 + 4 * x1 + x0)

    max_count(40)
    max_count(80)