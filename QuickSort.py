def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)
    
def quickSortHelper(alist, first, last):
    if first < last:
        splitPoint = partition(alist, first, last)
        
        quickSortHelper(alist, first, splitPoint-1)
        quickSortHelper(alist, splitPoint+1, last)
        
        
def partition(alist, first, last):
    base = alist[first]
    
    
    
    leftmark = first
    rightmark = last
    
    while leftmark < rightmark:  # 要求左指针必须小于等于右指针，之所以没有等号是因为，在最后一次指针移动的时候就会取等，
                                 # 不满足小于条件的时候其实已经取等了
        if alist[leftmark] <= base:
            leftmark += 1
        if alist[rightmark] >= base:
            rightmark -= 1
            
        else:      # 当左右指针都停止的时候，交换左右指针所对应的值
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
            
    # 当左指针和右指针重合的时候，交换右指针对应的值和base对应的值
    alist[rightmark], alist[first] = alist[first], alist[rightmark]
    
    return rightmark    # rightmark是作为递归排序的标记，所以返回。最后输出alist就是直接排序排好的
    
        
alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)   