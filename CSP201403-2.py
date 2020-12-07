
N,M = input().split()
N,M = int(N),int(M)
# 记录窗口
W = []
# i是窗口的编号
for i in range(1,N+1):
	w = list(map(int,input().split()))
	w.append(i)
	W.append(w)
# 以列表的索引顺序作为窗口的层级，
W.reverse()
for i in range(M):
    x, y = input().split()
    x,y = int(x),int(y)
    flag = 1
    for j,item in enumerate(W):
        if x>=item[0] and x<=item[2] and y>=item[1] and y<=item[3]:
            print(item[4])
            W.pop(j)
            W.insert(0,item)
            flag=0
            break
        else:
            continue
    if flag:
        print('IGNORED')