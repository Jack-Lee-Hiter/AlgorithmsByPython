'''
分治算法一般都伴随着递归算法
'''
# 分治算法实现查找数组中的最大元素的位置
def maxIndex(alist, start, end):
    if start > end or len(alist) == 0:
        return
    pivot = (start+end) >> 1
    if end - start == 1:
        return start
    else:
        temp1 = maxIndex(alist, start, pivot)
        temp2 = maxIndex(alist, pivot, end)
        if alist[temp1] < alist[temp2]:
            return temp2
        else:
            return temp1
print(maxIndex([5,7,9,3,4,8,6,2,0,1], 0, 9))

# 分治法计算正整数幂
def power(base, x):
    if x == 1:
        return base
    else:
        if x & 1 == 1:
            return power(base, x>>1)*power(base, x>>1)*base
        else:
            return power(base, x>>1)*power(base, x>>1)

print(power(2, 6))