def out_of_range(s, idx):
    if idx >= len(s):
        return True
    else:
        return False

def state1(s, idx):
    idx += 1
    if out_of_range(s, idx):
        return False
    if s[idx] == '1':
        return False
    elif s[idx] == '0':
        return state2(s, idx)

def state2(s,idx):
    idx += 1
    if out_of_range(s, idx):
        return False
    if s[idx] == '1':
        return False
    elif s[idx] == '0':
        return state3(s, idx)

def state3(s, idx):
    idx += 1
    if out_of_range(s,idx):
        return False
    if s[idx] == '1':
        return state4(s,idx)
    elif s[idx] == '0':
        return state3(s,idx)

def state4(s, idx):
    idx += 1
    if out_of_range(s, idx):
        return True
    if s[idx] == '1':
        return state4(s, idx) or state1(s, idx)
    elif s[idx] == '0':
        return state5(s,idx)

def state5(s, idx):
    idx += 1
    if out_of_range(s,idx):
        return False
    if s[idx] == '1':
        return state6(s,idx)
    elif s[idx] == '0':
        return False

def state6(s, idx):
    idx += 1
    if out_of_range(s,idx):
        return True
    if s[idx] == '1':
        return state1(s,idx)
    elif s[idx] == '0':
        return state5(s,idx)


n = int(input())
arr = []
for i in range(n):
    arr.append(input())

for tmp in arr:
    if tmp[0] == '1':
        if state1(tmp, 0):
            print("DANGER")
        else:
            print("PASS")
    else:
        if state5(tmp, 0):
            print("DANGER")
        else:
            print("PASS")
