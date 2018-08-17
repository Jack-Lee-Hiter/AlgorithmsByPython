# coding: utf-8

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
        while leftmark <= rightmark and alist[leftmark] <= pivotvlue: # bugfix: 先比较index, 不然数组会越界
            leftmark += 1
        while rightmark >= leftmark and alist[rightmark] >= pivotvlue:
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


if __name__ == "__main__":
    test_data = [3,2,111,3,-1,0,0,1,0,2,4]

    res_stable = sorted(test_data)
    quickSort(test_data)
    print(test_data)
    print(res_stable)
    assert all(map(lambda x: x[0] == x[1], zip(res_stable, test_data)))