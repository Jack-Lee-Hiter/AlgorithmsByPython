def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)

def quickSortHelper(alist, first, last):
    if first < last:
        splitPoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitPoint-1)
        quickSortHelper(alist, splitPoint+1, last)

def partition(alist, first, last):
    pivotvlue = alist[first]

    leftmark = first+1
    rightmark = last
    done = False

    while not done:
        while alist[leftmark] <= pivotvlue and leftmark <= rightmark:
            leftmark += 1
        while alist[rightmark] >= pivotvlue and rightmark >= leftmark:
            rightmark -= 1

        if leftmark > rightmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
    alist[rightmark], alist[first] = alist[first], alist[rightmark]
    return rightmark

alist = [54,26,93,17,77,31,44,55,20]
alist2 = [1]
quickSort(alist2)
print(alist2)
