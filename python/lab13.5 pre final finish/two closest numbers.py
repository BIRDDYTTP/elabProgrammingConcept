num1 = int(input())
x = num1+1
ls = []
chk_ls = []
count = 1
while count < x:
    num = int(input())
    ls.append(num)
    count += 1
count2 = 0
y = 0
while count2 < len(ls):
    count3 = count2+1
    while count3 < len(ls):
        ren = abs(ls[count2]-ls[count3])
        if count2 == 0 and count3 == 1:
            y = ren
        else:
            if ren < y:
                y = ren
        count3 += 1
    count2 += 1
count4 = 0
while count4 < len(ls):
    count5 = count4 + 1
    while count5 < len(ls):
        ren2 = ls[count4]-ls[count5]
        if abs(ren2) == y:
            if ren2 < 0 :
                chk_ls.append(ls[count4])
            elif ren2 > 0:
                chk_ls.append(ls[count5])
        count5 += 1
    count4 += 1
chk_ls.sort()
for x in chk_ls:
    print(x,x+y)