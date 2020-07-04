import sys

def merge(left, right):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i = i + 1
        elif left[i] >= right[j]:
            res.append(right[j])
            j = j + 1

    while j < len(right):
        res.append(right[j])
        j = j + 1

    while i < len(left):
        res.append(left[i])
        i = i + 1

    return res


def Merge_Sort(arr):
    if (len(arr) <= 1):
        return arr
    mid = len(arr) // 2
    leftarr = arr[:mid]
    rightarr = arr[mid:]
    leftarr = Merge_Sort(leftarr)
    rightarr = Merge_Sort(rightarr)
    return merge(leftarr, rightarr)


arr = list(map(int, input().split()))
print(Merge_Sort(arr))