# -*- coding:UTF-8 -*-
'''
神之算法-Manacher算法
求最长回文子串
'''


def manacher(s):
    if s == None or len(s) == 0:
        return
    # 预处理字符串, 把字符串中间和首尾都添加#号, 时的字符串长度变为奇数
    # 预处理后的字符串每个位置对应的最长回文串的半径 减去1 等于原始字符串该处对应的最长回文串的长度
    s = "#" + "#".join(s) + "#"
    curLongest = [0] * len(s)       # 使用curLongest存储每个位置最长回文串半径
    maxRight, mid = 0, 0            # maxRight, mid分别存储之前步骤中所有回文子串所能到达的s最右端坐标以及种鸽回文串的对称轴位置
    maxLen = 0                      # maxLen 记录当前的最长回文串的长度
    for i in range(len(s)):
        if i < maxRight:
            # i处于maxRight左边有两种情况
            # 1. 当前位置i和对称轴pos相对应的位置j在前面操作中拥有的最大回文串半径没有达到maxRight关于pos的对称位置, 此时curLongest[i]从curLongest[2 * mid - i]开始扩张
            # 2. 当前位置i和对称轴pos相对应的位置j在前面操作中拥有的最大回文串半径能够达到maxRight关于pos的对称位置, 此时curLongest[i]从maxRight-i的长度开始扩张
            curLongest[i] = min(curLongest[2 * mid - i], maxRight - i)
        else:
            # i处于maxRight的位置或者maxRight右边的位置时
            curLongest[i] = 1
        while i - curLongest[i] >= 0 and curLongest[i] + i < len(s) and s[i-curLongest[i]] == s[i+curLongest[i]]:
            curLongest[i] += 1
        # 如果当前i所对应的回文串最右边长度大于之前maxRight, 更新maxRight和对称轴的位置
        if curLongest[i] + i - 1 > maxRight:
            maxRight = curLongest[i] + i - 1
            mid = i
        maxLen = max(maxLen, curLongest[i])
    return maxLen - 1
print(manacher('saas'))