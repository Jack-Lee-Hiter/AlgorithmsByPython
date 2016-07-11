str1 = 'test python'
# 未使用正则表达式的查找
print(str1.find('1'))
print(str1.find('test'))
print(str1.startswith('test'))

# 使用正则表达式查找
import re
# 将正则表达式编译成pattern对象
# 使用r'test', r代表进行匹配的是元字符串
pa = re.compile(r'test')    # pa已经成为一个pattern实例
print(type(pa))

ma = pa.match(str1)         # 若匹配成功, ma成为一个match对象

print(ma)
print(ma.group())           # group()返回一个str或者tuple
print(ma.span())            # 返回字符串的索引
print(ma.re)                # pattern的实例

# 另一个例子
pa2 = re.compile(r'_')
ma2 = pa2.match('_value')

print(ma2.group())

# 例子3
pa3 = re.compile(r'_')
ma3 = pa3.match('value_')
# print(ma3.group())          #匹配失败   'NoneType' object has no attribute 'group'

# 忽略大小写匹配
pa = re.compile(r'test', re.I)      # re.I 忽略大小写, I=ignore
print(pa)

ma = pa.match('Test python')
print(ma.group())

#
ma = re.match(r'test', 'Test Python', re.I)
print(ma.group())