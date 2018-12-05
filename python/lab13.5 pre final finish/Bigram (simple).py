line = int(input())
count = 1 
ls = []
while count <= line:
    chck = []
    bj = str(input())
    for x in bj:
        a = ''
        if x != ' ':
            a += x
        else:
            chck.append(a)
            a = ''
    count2 = 0
    while count2 <= 4:
        z = chck[count2]
        if z == 'A':
            chck[count2] = 1
        elif z == 'J' or z == 'Q' or z == 'K':
            chck[count2] = 10
        else:
            chck[count2] = int(chck[count2])
    aa = chck[0]+chck[1]+chck[2]
    if aa > 16:
        ls.append(aa)
    else:
        ls.append(sum(chck))
    count += 1
    print(chck)
print(ls)