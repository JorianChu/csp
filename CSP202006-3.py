#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/8/15  15:03
"""
w = int(input())
# global line_temp,newline_ch_nums,w,count,ans
line_temp = ""
ans = []
newline_ch_nums = 0
count = 0

def add_ch(ch):
    line_temp += ch
    newline_ch_nums += 1
    if newline_ch_nums==w:
        ans[count] = line_temp
        count += 1
        line_temp = ""
        newline_ch_nums = 0



def markdown_render():
   
    # 0:段落 1:列表 2:空行，flag1为上一行标志，flag2为本行标志
    flag1 = flag2 = 0
    count = newline_ch_nums = 0
    ans = []
    fg = 0
    line_temp = ""
    for _ in range(w):
        line = input()
        # 是否是空行
        if line.strip() == '':
            flag1 = 2
            continue
        if flag1==2 and fg:
            ans[count] = ""
            count += 1
        flag2 = 0
        # 项目开始
        if len(line)>=2 and line[0]=='*' and line[1]==' ':
            flag2 = 1
            # 去除开头两个字符
            line = line[2:]
            if flag1==1 and newline_ch_nums!=0:
                count += 1
                ans[count] = line_temp
                line_temp = ""
                newline_ch_nums = 0
        elif len(line)>=2 and line[0]==' ' and line[1]==' ':
            # 上一行是列表
            if flag1==1:
                line = line[2:]
                flag2 = 1
                if newline_ch_nums==0:
                    # 添加三个字符
                    # line_temp += "+++"
                    add_ch("+")
                    add_ch("+")
                    add_ch("+")
                    newline_ch_nums += 3
        line = line.strip()
        # 删除首尾空格
        line = line.strip()
        if flag1==0:
            if flag2==0 and num!=0:
                add(' ')
        if flag2==1:
            if flag2==0:
                #且空行
                pass
            if flag2 == 1:
                if num>3:
                    add(' ')
        for j



        article.append(input())


