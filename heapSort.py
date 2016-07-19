def heapSort(alist):
    if alist == None or len(alist) == 0:
        return
    length = len(alist)
    output = []
    for i in range(length):
        tempLen = len(alist)
        for j in range((tempLen-1)//2, -1, -1):
            k = j
            v, heap = alist[k], False
            while not heap and 2*k <= tempLen-1:
                index = 2 * k
                if index < tempLen-1:
                    if alist[index] < alist[index+1]:
                        index += 1
                if v >= alist[index]:
                    heap = True
                else:
                    alist[k] = alist[index]
                    k = index
            alist[k] = v
        heapVal = alist.pop(0)
        output.insert(0, heapVal)
    return output

test = [2, 6, 5, 9, 10, 3, 7]
print(heapSort(test))