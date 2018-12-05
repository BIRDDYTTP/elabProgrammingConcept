num = int(input())
ls = []
while num != 0:
    ls.append(num)
    num = int(input())
count = 0
a = 0
while count <= len(ls)-1:
    count2 = 0
    while count2 <= len(ls)-1:
        b = sum(ls[count:count2+1])
        if b > a:
            a = b
        count2 += 1
    count += 1
print(a)