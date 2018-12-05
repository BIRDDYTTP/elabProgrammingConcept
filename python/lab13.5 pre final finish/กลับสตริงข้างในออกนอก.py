st = str(input())
a = ''
count = len(st)
if len(st) % 2 == 0:
    x = (count // 2)-1
    while x >= 0:
        a += st[x]
        x -= 1
    y = len(st)-1
    while y >= count//2:
        a += st[y]
        y -= 1
else:
    x = (count // 2)-1
    while x >= 0 :
        a += st[x]
        x -= 1
    a += st[count//2]
    y = len(st)-1
    while y >= (count//2)+1:
        a += st[y]
        y -= 1
print(a)
