#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/7/3  21:11
"""
# 工资计算
# 根据税后工资计算税前工资

# 税前工资S
# 税后工资

# 3500
# 收税
# 45（3%）,45+300=345（10%）,345+900=1245（20%）,
# 1245+6500=7745（25%）,7745+6000=13745(30%),
# 13745+8750=22445(35%),

# 3500,4955，7655，11255，30755，44755，61055

# 9255-3500=5755

salary = [3500, 5000, 8000, 12500, 38500, 58500, 83500, 100000]
cost = [0,0.03,0.1,0.2,0.25,0.3,0.35,0.45]
salary_af = []
# 计算每个工资段的最大税后工资
for i in range(len(salary)):
    if i==0:
        temp = 3500
    else:
        temp += int((salary[i]-salary[i-1])*(1-cost[i]))
    salary_af.append(temp)

T = int(input())
S=0
for i in range(len(salary)):
    if T<=salary_af[i]:
        if i==0:
            S = T
            break
        else:
            S = salary[i-1]+(T-salary_af[i-1])/(1-cost[i])
            break
print(int(S))
        # for j in range(i):

        # for j in range(i):
