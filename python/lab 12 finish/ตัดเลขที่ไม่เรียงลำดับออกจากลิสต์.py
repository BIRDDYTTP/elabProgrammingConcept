num = int(input())
ls = []
while num != -1:
    ls.append(num)
    num = int(input())
count = 0
ls2 = []
while count <= len(ls)-1:
    if count >0:
        if ls[count] > ls[count-1]:
            ls2.append(ls[count])
            count += 1
        else:
            ls.remove(ls[count])
    else:
        ls2.append(ls[count])
        count += 1
print(ls2)