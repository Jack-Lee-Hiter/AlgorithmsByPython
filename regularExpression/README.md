# 正则表达式
1. 使用单个字符串来描述匹配一系列符合某个句法规则的字符串。
2. 是对字符串操作的一种逻辑公式
3. 应用场景：处理文本和数据
4. 正则表达式过程：依次拿出表达式和文本中的字符比较，如果每一个字符都能匹配， 则匹配成功；否则匹配失败。

## Python下使用正则表达式
1. `import re`：正则表达式模块：Python通过re模块提供对正则表达式的支持。使用re的一般步骤是先将正则表达式的字符串形式编译为Pattern实例，然后使用Pattern实例处理文本并获得匹配结果（一个Match实例），最后使用Match实例获得信息，进行其他的操作。r代表进行匹配的是元字符串， 不使用元字符串则需要注意转译的情况。

使用正则表达式匹配字符串开头是否为指定的字符或字符串：


```
import re
str1 = 'test python'
# 将正则表达式编译成pattern对象
# 使用r'test', r代表进行匹配的是元字符串
pa = re.compile(r'test')    # pa已经成为一个pattern实例
print(type(pa))

ma = pa.match(str1)         # 若匹配成功, ma成为一个match对象

print(ma)
print(ma.group())           # group()返回一个str或者tuple
print(ma.span())            # 返回字符串的索引
print(ma.re)                # pattern的实例
```

```
# 返回结果
<class '_sre.SRE_Pattern'>
<_sre.SRE_Match object; span=(0, 4), match='test'>
test
(0, 4)
re.compile('test')
```

## 正则表达式语法


|字符|匹配|
|------|------|
|.|匹配任意字符(除了\n)|
|[...]|匹配字符集|
|\d / \D|匹配数字/非数字|
|\s / \S|匹配空白/非空白字符|
|\w / \W|匹配单词字符[a-zA-Z0-9]/非单词字符|
|\*|匹配前一个字符0次或者无限次|
|+|匹配前一个字符1次或者无限次|
|？|匹配前一个字符0次或1次|
|{m}/{m,n}|匹配前一个字符m次或者n次|
|{m,}|匹配前一个字符m次或更多次|
|\*? / +? / ??|匹配模式变为非贪婪(尽可能少匹配字符|)
|^|匹配字符串开头|
|$|匹配字符串结尾|
|\A / \Z|指定的字符串匹配必须出现在开头/结尾|
|\||匹配左右任意一个表达式|
|(ab)|括号中表达式作为一个分组|
|\\\<number>|引用编号为num的分组匹配到的字符串|
|(?P\<name>)|分组起一个别名|
|(?P=name)|引用别名为name的分组匹配字符串|

## Python正则表达式--re模块其他方法
1. search(pattern, string, flags=0)在一个字符串中查找匹配
2. findall(pattern, string, flags=0)找到匹配，返回所有匹配部分的列表
3. sub(pattern, repl, string, count=0, flags=0)将字符串中匹配正则表达式的部分替换为其它值
4. split(pattern, string, maxsplit=0, flags=0)根据匹配分割字符串， 返回分割字符串组成的列表

## re练习
利用正则表达式尝试抓取了20160711[腾讯网](http://www.qq.com/)上的jpg和png图像。