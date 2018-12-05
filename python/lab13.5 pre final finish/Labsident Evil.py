dammage = int(input())
ls = []
ls2 = []
c_ls = []
z = str(input())
st = ''
for x in z:
    ls.append(x)
for x in ls:
    if x != ' ':
        st += x
    else:
        ls2.append(int(st))
        st = ''
ls2.append(int(st))
count = 0
for x in ls2:
    if x % dammage == 0:
        count += (x//dammage)
        c_ls.append(count)
    else:
        count += (x//dammage+1)
        c_ls.append(count)
print(count)
for x in c_ls:
    print(x,end=' ')
    