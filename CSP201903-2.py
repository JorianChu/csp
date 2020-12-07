#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/7/6  9:06
"""

def cal_express(express):
	express = list(express)
	temp = []
	for i,ch in enumerate(express):
		if ord(ch)>=48 and ord(ch)<=57:
			num = int(ch)
			temp.append(num)
		else:
			if ch=='+' or ch=='-':
				temp.append(ch)
			else:
				a = temp.pop()
				b = int(express.pop(i+1))
				if ch=='x':
					temp.append(a*b)
				else:
					temp.append(a//b)
	ans = temp[0]
	for i in range(1,len(temp),2):
		if temp[i]=='+':
			ans += temp[i+1]
		else:
			ans -= temp[i+1]
	return ans


N = int(input())
for i in range(N):
	if cal_express(input())==24:
		print("Yes")
	else:
		print("No")