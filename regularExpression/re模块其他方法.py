import re

str1 = 'study time = 1000'

print(str1.find('1000'))

# 如果数字1000发生变化, 可以使用正则表达式的search查找数组, 其中\d+就是匹配任意多字符的数字
# search仅能查找第一个符合项
info = re.search(r'\d+', str1)
print(info.group())

str1 = 'study time = 10000'
info = re.search(r'\d+', str1)
print(info.group())

# findall 能查找到所有匹配项, 返回值为一个list
str2 = 'python code num = 100, swift code num = 50, c++ code num = 10'
info = re.findall(r'\d+', str2)
print(info)
print(sum([int(x) for x in info]))

# sub将字符中匹配正则表达式的部分替换为其它值
str3 = 'python num = 1000'
info = re.sub(r'\d+', '1001', str3)         # 将str3中的数字替换为1001
print(info)

# 利用函数将str3中的数字加1
def add(match):
    val = match.group()
    num = int(val) + 1
    return str(num)

info = re.sub(r'\d+', add, str3)
print(info)

# split
str4 = 'class=C C++ Java Python, C#'
info = re.split(r'=| |,', str4)
print(info)