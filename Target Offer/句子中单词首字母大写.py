'''
面试题：
一个句子的所有单词的首字母大写，其余小写
'''
def title(s):
    if not s:
        return ""
    res = ""
    diff = ord("a") - ord("A")
    for i in range(1, len(s)):
        if s[i-1] == " " and s[i] <= "z" and s[i] >= "a":
            res += chr(ord(s[i]) - diff)
        elif s[i-1] != " " and s[i] <= "Z" and s[i] >= "A":
            res += chr(ord(s[i]) + diff)
        else:
            res += s[i]
    if s[0] <= "z" and s[0] >= "a":
        res = chr(ord(s[0]) - diff) + res
    else:
        res = s[0] + res
    return res

def title2(s):
    return s.title()

print(title2(" sDsa sddr jki "))