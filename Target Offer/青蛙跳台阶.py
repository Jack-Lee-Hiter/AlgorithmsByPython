'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''


'''
这是一个斐波那契数列的变种，f(1) = 1; f(2) = 2;
f(n) = f(n-1) + f(n-2)
'''
class Solution:
    def jumpFloor(self, number):
        tempArray = [1, 2]
        
        if number >= 3:   # number是从3开始迭代的
            for i in range(3, number + 1):
                tempArray[(i + 1)% 2] = tempArray[0] + tempArray[1]  # 3应当时更正tempArray的第一个位置，所以i+1
        return tempArray[(number + 1) %2]


test = Solution()
test.jumpFloor(100)       