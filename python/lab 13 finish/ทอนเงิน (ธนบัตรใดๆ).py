num = int(input())
count = 1
ls = []
while count <= num :
    bank = int(input())
    ls.append(bank)
    count += 1
ls.sort(reverse=True)
money = int(input())
ls2 = []
for x in ls:
    ls2.append(money//x)
    money = money % x
count2 = 0
while count2 < len(ls):
    print('%d: %d' %((ls[count2]),(ls2[count2])))
    count2 += 1