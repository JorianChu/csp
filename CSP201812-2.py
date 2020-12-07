r,y,g = map(int,input().split())
N = int(input())

def cal_time(k,t,sum):
	if k==0:
		return k,t
	#计算到达路口时，一轮循环（红-》绿-》黄）下的从红灯开始经过的时间
	t_temp = sum%(r+g+y)
	if t_temp<t:
	#t-t_temp为距离红灯结束的倒计时时间(需要等待)
		return k,t-t_temp
	else:
		if k==1:
			#到达路口时，红灯已过，接下来是绿灯
			return cal_time(3,g,t_temp-t)
		elif k==2:
			return cal_time(1,r,t_temp-t)
		else:
			return cal_time(2,y,t_temp-t)

sum =0
for i in range(N):
	k,t = map(int,input().split())
	a,b = cal_time(k,t,sum)
	if a==0 or a==1:
		sum += b
	elif a==2:
		sum += b+r
print(sum)
