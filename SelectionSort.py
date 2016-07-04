# 选择排序, 纯粹练手 - -||
def selectionSort(alist):
    for i in range(len(alist)-1):
        min = i
        for j in range(i+1, len(alist)):
            if alist[j] < alist[min]:
                min = j
        alist[i], alist[min] = alist[min], alist[i]
    return alist

alist = [54,26,93,17,77,31,44,55,20]
print(selectionSort(alist))