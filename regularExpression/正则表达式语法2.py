import re
# | 匹配左右任意一个表达式
ma = re.match(r'abc|d', 'abc')
print(ma.group())
ma = re.match(r'abc|d', 'd')
print(ma.group())

# 匹配0-99的任意字符串
ma = re.match(r'[1-9]?\d$', '99')
print(ma.group())
# 匹配0-100的任意字符串
ma = re.match(r'[1-9]?\d$|100', '100')
print(ma.group())

# 匹配一个163或者126的邮箱
ma = re.match(r'[\w]{4,6}@(163|126).com', 'abc89@126.com')
print(ma.group())

# 匹配<book>
ma = re.match(r'<[\w]+>', '<book>')
print(ma.group())
ma = re.match(r'<([\w]+>)', '<book>')       # ()括住的是一个分组, 使用时注意是groups()而不是group()
print(ma.groups())
ma = re.match(r'<([\w]+>)\1', '<book>book>')    # 匹配 book>book> 的第一个分组, 下面写的时候又是group()而不是groups()
print(ma.group())
# 匹配一个<book>python</book>
# <([\w]+>)[\w]+</\1 中, 第一个<就是第一个左尖括号, ([\w]+>)表示匹配任意多次 [\w]+>, 这些任意多次 [\w]+> 组成一个元组
# [\w]+</ 分为两部分, [\w]+ 表示任意多次 \w, 即这里的 python 字符串, 然后再匹配 <\
# 最后 \1 匹配第一个分组, 即 ([\w]+>) 所对应的内容, 即 book>
ma = re.match(r'<([\w]+>)[\w]+</\1', '<book>python</book>')
print(ma.group())

# ?P<mark> 是给分组起的名字, (?P=mark) 引用名称为mark的分组
ma = re.match(r'<(?P<mark>[\w]+>)[\w]+</(?P=mark)', '<book>python</book>')
print(ma.group())