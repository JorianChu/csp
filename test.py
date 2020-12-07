
str1 = '  '
str2 = '  ' \
       ''

if str1.strip(str2)=='':
    print("yes")

def judeg_sp(line):
    return line.strip() == ''

def add_ch():
    pass
print(judeg_sp(str2))