import re

ma = re.match(r'a', 'a')
print(ma.group())

# 使用 '.' 匹配任意字符
ma = re.match(r'.', 'b')
print(ma.group())

ma = re.match(r'{.}', '{a}')    # 匹配大括号中的任意一个字符
print(ma.group())

ma = re.match(r'{..}', '{ab}')  # 匹配大括号中的任意两个字符
print(ma.group())

# 使用 [...] 匹配字符集
ma = re.match(r'{[abc]}', '{a}') # 匹配大括号中为a或b或c的值
print(ma.group())

ma = re.match(r'{[a-z]}', '{d}') # 匹配a-z的任意一个字符
print(ma.group())

ma = re.match(r'{[a-zA-Z]}', '{Z}')
print(ma.group())

ma = re.match(r'{[\w]}', '{0}') # 使用`\w`匹配a-zA-Z0-9的任意一个字符
print(ma.group())

# 对于中括号中的匹配, 需要加一个转意
ma = re.match(r'\[[\w]\]', '[a]')   # '\['和'\]'用来转意
print(ma.group())

ma = re.match(r'[A-Z][a-z]', 'Aa')
print(ma.group())

ma = re.match(r'[A-Z][a-z]*', 'A') # 匹配一个大写字母和0个或无穷多个小写字母
print(ma.group())
ma = re.match(r'[A-Z][a-z]*', 'Aa')
print(ma.group())
ma = re.match(r'[A-Z][a-z]*', 'Aafdsfdsb')
print(ma.group())
ma = re.match(r'[A-Z][a-z]*', 'Aafdsfdsbadfas154154')       # 此例子只匹配数字前的字符
print(ma.group())

# 匹配以至少一个为_或者a-z或者A-Z开头的字符, 后面接无线多个_或者a-z或者A-Z。可以用于检测变量名是否合法
# 注意这里 + 代表的是匹配前一个字符1次或者无限次
ma = re.match(r'[_a-zA-Z]+[_\w]*', '__init')
print(ma.group())

ma = re.match(r'[1-9]?[0-9]', '99')             # 按照正常显示0-99的匹配, 09匹配不上, 9可以匹配上。?代表匹配一次或者0次
print(ma.group())

ma = re.match(r'[1-9]?[0-9]', '09')                 # 返回 0 , 不是09
print(ma.group())

ma = re.match(r'[a-zA-Z0-9]{6}', 'bac123')          # a-zA-Z0-9匹配六次
print(ma.group())
# ma = re.match(r'[a-zA-Z0-9]{6}', 'bac12')       # 返回空, 因为bac12长度小于6
# print(ma.group())
ma = re.match(r'[a-zA-Z0-9]{6}', 'bac1234')         # bac123
print(ma.group())

# 长度为6的163邮箱匹配
ma = re.match(r'[a-zA-Z0-9]{6}@163.com', 'abc123@163.com')
print(ma.group())
# 程度为6-10的163邮箱匹配
ma = re.match(r'[a-zA-Z0-9]{6,10}@163.com', 'abc123gd@163.com')
print(ma.group())

ma = re.match(r'[0-9][a-z]*?', '1bc')               # 只匹配第一个1, 采取非贪婪模式, 尽可能少匹配
print(ma.group())

ma = re.match(r'[0-9][a-z]+?', '1bc')               # 1b
print(ma.group())

# 匹配字符串的开头或者结尾
ma = re.match(r'[\w]{4,10}@163.com', 'abc123gd@163.comabc')         # abc123gd@163.com 但是原始字符串不是我们想要的
print(ma.group())
# ma = re.match(r'[\w]{4,10}@163.com$', 'abc123gd@163.comabc')    # 报错, 加上$后, 结尾必须是@163.com
# print(ma.group())

ma = re.match(r'^[\w]{4,10}@163.com$', 'abc123gd@163.com')          # 前面加上 ^  , 必须以[\w]开头
print(ma.group())


ma = re.match(r'\Aabc[\w]{4,10}@163.com$', 'abc123gd@163.com')      # \A 限定了开头必须以 abc 开头
print(ma.group())