#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/27 17:21
# @Version : 1.1
# @Author  : Jade
# @File    : 201912-3.py
# @Software: PyCharm
# 化学方程式
#
import re

def bracketsMatch(text):
    # 括号匹配
    text_len = len(text)
    stack = list()
    brackets_dict = {}
    for i in range(text_len):
        if(text[i] == '('):
            stack.append(i)
        elif(text[i] == ')'):
			# {1:5,2:4}...
            brackets_dict[stack.pop()] = i
    return brackets_dict

def getRatio(text,left,right):
    # 得到系数
    if(left >= right):
        return 1,left
    i,dit = left,0
    while(i < right and text[i].isdigit()):
        dit = dit*10 + int(text[i])
        i += 1
    return max(1,dit),i

def getElem(text,left,right):
    # 得到元素
    if(text[left].isupper()):
        if(left + 1 < right and text[left+1].islower()):
                return text[left:left+2],left+2
        return text[left:left+1],left+1
    return None,left

def readElement(text,brackets,left,right):
    # 递归
    elem_dict = {}
    while(left < right):
        elem_dict1 = dict()
        if(text[left] == '('):
			# 把子节点抽出来
            elem_dict1 = readElement(text,brackets,left+1,brackets[left])
            left = brackets[left] + 1
        else:
            elem,left = getElem(text,left,right)
            elem_dict1 = {
                elem:1
            }
        ratio,left = getRatio(text,left,right)
        # print(ratio,left)
        for k in elem_dict1.keys():
            elem_dict[k] = elem_dict.get(k,0) +  ratio * elem_dict1.get(k,0)
    # print(elem_dict)
    return elem_dict

def elemFor(text):
    elem_dict = dict()
    for elem in text.split("+"):
        brackets = bracketsMatch(elem)
        ratio, left = getRatio(elem, 0, len(elem))
        elem_dict1 = readElement(elem,brackets,left,len(elem))
        for key in elem_dict1.keys():
            elem_dict[key] = ratio * elem_dict1.get(key,0) + elem_dict.get(key,0)
    return elem_dict

def judge(left_dict,right_dict):
    #判断是否相等
    # print(left_dict,right_dict)
    for key in left_dict.keys():
        if(left_dict.get(key,0) != right_dict.get(key,0)):
            return False
    for key in right_dict.keys():
        if (left_dict.get(key, 0) != right_dict.get(key, 0)):
            return False
    return True

def main():
    n = int(input())
    for _ in range(n):
        left_text,right_text = input().split('=')
        left_dict = elemFor(left_text)
        right_dict = elemFor(right_text)
        print("%s"%('Y' if judge(left_dict,right_dict) else 'N'))

if __name__ == '__main__':
    main()
"""
11
H2+O2=H2O
2H2+O2=2H2O
H2+Cl2=2NaCl
H2+Cl2=2HCl
CH4+2O2=CO2+2H2O
CaCl2+2AgNO3=Ca(NO3)2+2AgCl
"""

