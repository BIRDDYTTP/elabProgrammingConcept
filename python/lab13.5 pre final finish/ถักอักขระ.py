st = str(input())
op = ''
a = len(st)
if a%2 == 0:
    b = 1
    while b <= a//2:
        op += st[b-1]
        op += st[a-b]
        b += 1
else:
    b = 1
    while b <= a//2+1:
        if b == a//2+1:
            op += st[b-1]
        else:
            op += st[b-1]
            op += st[a-b]
        b += 1
print(op)