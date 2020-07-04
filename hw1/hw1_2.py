import sys

def QuickSort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    s=[]
    e=[]
    b=[]

    for i in arr:
        if i<pivot:
            s.append(i)
        elif i==pivot:
            e.append(i)
        else:
            b.append(i)

    arr= QuickSort(s)+e+QuickSort(b)
    return arr

arr = list(map(int, input().split()))
print(QuickSort(arr))