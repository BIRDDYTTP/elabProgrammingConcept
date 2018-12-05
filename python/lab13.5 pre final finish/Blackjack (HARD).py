line = 1
count = 1 
ls = []
while count <= line:
    a = []
    bj = str(input())
    a.append(bj)
    ls.append(a)
    count += 1
chck = []
for x in ls:
    b = ''
    chck2 = []
    for y in x:
        for z in y:
            if z == ' ':
                chck2.append(b)
                b = ''
            else:
                b += z
    chck2.append(b)
    chck.append(chck2)
ans = []
check = []
for z in chck:
    e = 0
    for q in z:
        if e > 16:
            break
        else:
            if q == 'A':
                e += 1
            elif q == 'J' or q == 'Q' or q == 'K':
                e += 10
            elif q.isdigit() == True:
                e += int(q) 
            check.append(q)
    ans.append(e)
checklist = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
c = 0
for a in check:
    b = checklist.index(a)
    if b > c:
        c = b
print(checklist[c])
for p in ans:
    if p > 21:
        print('busted')
    else:
        print(p)