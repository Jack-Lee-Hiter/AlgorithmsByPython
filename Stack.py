# Python3.5
# 定义一个栈类
class Stack():
    # 栈的初始化
    def __init__(self):
        self.items = []
    # 判断栈是否为空,为空返回True
    def isEmpty(self):
        return self.items ==[]
    # 向栈内压入一个元素
    def push(self, item):
        self.items.append(item)
    # 从栈内推出最后一个元素
    def pop(self):
        return self.items.pop()
    # 返回栈顶元素
    def peek(self):
        return self.items[len(self.items)-1]
    # 判断栈的大小
    def size(self):
        return len(self.items)

# 栈属性测试
# 测试数据
# s = Stack()
# print(s.isEmpty())
# s.push(4)
# s.push('dog')
# print(s.peek())
# s.push(True)
# print(s.isEmpty())
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.size())

# 利用栈将字串的字符反转
def revstring(mystr):
    # your code here
    s = Stack()
    outputStr = ''
    for c in mystr:
        s.push(c)
    while not s.isEmpty():
        outputStr += s.pop()
    return outputStr

# print(revstring('apple'))
# print(revstring('x'))
# print(revstring('1234567890'))

# 利用栈判断括号平衡Balanced parentheses
def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open, close):
    opens = '([{'
    closers = ')]}'
    return opens.index(open) == closers.index(close)

# print(parChecker('({([()])}){}'))

# 利用栈将十进制整数转化为二进制整数
def Dec2Bin(decNumber):
    s = Stack()

    while decNumber > 0:
        temp = decNumber % 2
        s.push(temp)
        decNumber = decNumber // 2
    binString = ''
    while not s.isEmpty():
        binString += str(s.pop())
    return binString

# print(Dec2Bin(42))

# 利用栈实现多进制转换
def baseConverter(decNumber, base):
    digits = '0123456789ABCDEF'

    s = Stack()

    while decNumber > 0:
        temp = decNumber % base
        s.push(temp)
        decNumber = decNumber // base

    newString = ''
    while not s.isEmpty():
        newString = newString + digits[s.pop()]

    return newString

# print(baseConverter(59, 16))

# 利用栈实现普通多项式的后缀表达式
def infixToPostfix(infixexpr):
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return ''.join(postfixList)

# print(infixToPostfix("A * B + C * D"))
# print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))

