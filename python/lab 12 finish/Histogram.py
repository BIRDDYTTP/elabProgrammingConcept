score = int(input('Enter score: '))
sc_ls = []
check_ls = [0,1,2,3,4,5,6,7,8,9,10]
ls = []
count = 2
while count <= 20:
    if score <= 10 and score >= 0:
        sc_ls.append(score)
        count += 1
    else:
        print('score is out of range.')
        break
    score = int(input('Enter score: '))
sc_ls.append(score)
count2 = 0
while count2 < 11:
    a = 0
    for x in sc_ls: 
        if x == check_ls[count2]:
            a += 1
    ls.append(a)
    count2 += 1
print('Original list:')
print(sc_ls)
a = 0
while a < 11:
    print('%2d' %(check_ls[a]) , '*'*ls[a])
    a += 1