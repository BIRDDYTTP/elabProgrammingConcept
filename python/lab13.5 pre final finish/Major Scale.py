major = str(input())
num = int(input())
ls = []
a = ''
for x in major:
    if x != ',':
        a += x
    else:
        ls.append(a)
        a = ''
ans = num % len(ls)-1
print(ls[ans])