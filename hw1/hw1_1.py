import sys
arr = list(map(int, input().split()))
num = int(input())

lowIdx = 0
highIdx = len(arr)-1
while lowIdx <= highIdx:
    midIdx = int((lowIdx+highIdx)/2)
    if arr[midIdx] > num:
        highIdx = midIdx-1
    elif arr[midIdx] < num:
        lowIdx = midIdx+1
    else:
        print(midIdx+1)
        sys.exit()
print(None)