#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/8 14:08
# @Version : 1.1
# @Author  : Jade
# @File    : 201912-4.py
# @Software: PyCharm
#

import copy

def init(n):
    edge = list()
    for i in range(n):
        edge.append([])
    edge.append([])
    # i = 1 : n 
    return edge


def main():
    n,m = map(int,input().split())
    edges = init(n)
    info_list = init(n)
     # info[n+1][5454]
    for i in range(n):
        info_list[i+1].append(0)

    for _ in range(m):
        u,v = map(int,input().split())
        edges[u].append(v)
        edges[v].append(u)

    t,k = map(int,input().split())
    queue = list()
    # stl stack queue  heapc
    for _ in range(k):
        input_list = list(map(int,input().split()))
        a , b = input_list[0] , input_list[1]
        # (info_list , input_time , node_id)
        while(len(queue) != 0 and queue[0][1] + t <= b):
            u = queue[0][-1]
            pre_t = queue[0][1]
            pre_info = queue[0][0]
            for v in edges[u]:
                if (len(pre_info) > len(info_list[v]) or ( len(pre_info) == len(info_list[v]) and pre_info[-1] < info_list[v][-1])):
                    info_list[v] = copy.deepcopy(pre_info)
                    queue.append((copy.deepcopy(pre_info), pre_t + t, v))
            del queue[0]
        if(len(input_list) == 2):
            print(len(info_list[a]),' '.join(map(str,info_list[a])))
        else:
            info_list[a].append(input_list[-1])
            queue.append((info_list[a], b, a))


if __name__ == '__main__':
    main()

"""
5 10
1 2
1 3
1 4
1 5
2 3
2 4
2 5
3 4
3 5
4 5
1 27
1 1 1
2 1 2
3 1 3
4 1 4
5 1 5
1 1
2 1
3 1
4 1
5 1
1 2
2 2
3 2
4 2
5 2
1 10 10
2 11 9
1 11
2 11
3 11
4 11
5 11
1 12
2 12
3 12
4 12
5 12
"""