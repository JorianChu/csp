#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/8/8  14:06
"""

# import re
def splitAdd(arr):
    item_arr = list(arr.split('+'))
    return item_arr

def getElem(elem):
    elem_dic = {}
    first_num = 1
    if elem[0].isdigit():
        first_num = int(elem[0])
    flag = 0
    for i in range(len(elem)):
        if elem[i].islower():
            elem_dic[elem[i-1:i+1]] = 1
            elem_dic.pop(elem[i-1])
            flag = 1
        elif elem[i].isdigit():
            if i==0:
                continue
            if i!=0 and flag:
                elem_dic[elem[i-2:i]] = int(elem[i])
                flag = 0
            else:
                elem_dic[elem[i-1]] = int(elem[i])
        else:
            elem_dic[elem[i]] = 1
    for key in elem_dic.keys():
        elem_dic[key] *= first_num
    return elem_dic

def dealBrace(elem):
    pass


def judgeEquel(temp):
    left_chem,right_chem = temp.split('=')
    left_chem_arr = splitAdd(left_chem)
    right_chem_arr = splitAdd(right_chem)
    left_elem_dic = {}
    for i in range(len(left_chem_arr)):
        elem_dic_temp = getElem(left_chem_arr[i])
        for key,value in elem_dic_temp.items():
            if key in left_elem_dic.keys():
                left_elem_dic[key] += value
            else:
                left_elem_dic[key] = value

    right_elem_dic = {}
    for i in range(len(right_chem_arr)):
        elem_dic_temp = getElem(right_chem_arr[i])
        for key,value in elem_dic_temp.items():
            if key in right_elem_dic.keys():
                right_elem_dic[key] += value
            else:
                right_elem_dic[key] = value


    if len(left_elem_dic)!=len(right_elem_dic):
        # return "N"
        print("N")
        return
    for key in left_elem_dic.keys():
        if key not in right_elem_dic.keys():
            # return "N"
            print("N")
            return
        if left_elem_dic[key] != right_elem_dic[key]:
            # return "N"
            print("N")
            return
    # return "Y"
    print("Y")
    return

n = int(input())
ans = []
for i in range(n):
    str = input()
    if '(' in str:
    # if re.search(r'\(',str):
        # ans.append("Y")
        print("Y")
    else:
        # ans.append(judgeEquel(str))
        judgeEquel(str)

# for i in range(n):
#     print(ans[i])


str = 'H2+O2=H2O'
str1 = 'Cu=Cu'
str2 = "CH4+2O2=CO2+2H2O"
str3 = "CaCl2+2AgNO3=Ca(NO3)2+2AgCl"
str4 = "4Au+8NaCN+2H2O+O2=4Na(Au(CN)2)+4NaOH"
str5 = "4Zn+10HNO3=4Zn(NO3)2+NH4NO3+3H2O"
str6 = "3Ba(OH)2+2H3PO4=Ba3(PO4)2+6HZO"

'''
H2+O2=H2O
2H2+O2=2H2O
H2+Cl2=2NaCl
H2+Cl2=2HCl
CH4+2O2=CO2+2H2O
CaCl2+2AgNO3=Ca(NO3)2+2AgCl
3Ba(OH)2+2H3PO4=6H2O+Ba3(PO4)2
3Ba(OH)2+2H3PO4=Ba3(PO4)2+6H2O
4Zn+10HNO3=4Zn(NO3)2+NH4NO3+3H2O
4Au+8NaCN+2H2O+O2=4Na(Au(CN)2)+4NaOH
Cu+As=Cs+Au
'''


# judgeEquel(str)
# judgeEquel(str1)
# judgeEquel(str2)
# judgeEquel(str3)
# judgeEquel(str4)
# judgeEquel(str5)
# judgeEquel(str6)



