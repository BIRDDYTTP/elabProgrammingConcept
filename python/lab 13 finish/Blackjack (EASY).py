line = int(input())
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
    ans.append(e)
for p in ans:
    if p > 21:
        print('busted')
    else:
        print(p)