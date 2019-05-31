'''
和青蛙跳台阶问题类似，再做出一定程度扩展。

一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

这个问题写起来就很简单了，由数学归纳我们可以知道，一共有2^(n-1)种方案，所以就可以直接写代码
'''

class Solution:
    def jumpFloor2(self, number):
        if number == 0:
            return 0
        
        ans = 1
        if number == 1:
            return 1
        else:
            for i in range(1, number):
                ans = 2*ans
            return ans