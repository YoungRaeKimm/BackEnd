class lec:
    def __init__(self, num, start, end):
        self.num = num
        self.start = start
        self.end = end

    def __lt__(self, other):
        if self.end == other.end:
            return self.start < other.start
        else:
            return self.end < other.end


num_of_lectures = int(input())
lectures = []
for i in range(num_of_lectures):
    tmp = list(map(int, input().split()))
    tmplec = lec(tmp[0], tmp[1], tmp[2])
    lectures.append(tmplec)
lectures = sorted(lectures)
resarr = []
last_end_time = 0
for i in lectures:
    if(last_end_time <= i.start):
        last_end_time = i.end
        resarr.append(i)
print(len(resarr))
tmp = []
for i in resarr:
    tmp.append(i.num)
print(tmp)