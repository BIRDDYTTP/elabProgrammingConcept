a = str(input())
check_ls = []
while a != -1 :
    s = ''
    b = ''
    c = ''
    for x in a:
        if x == '=':
            b += ' = '
        elif b == ' = ':
            c += x
        else:
            s += x
    z = s.strip(' ') + b + c.strip(' ')
    check_ls.append(z)
    a = str(input())
y = 0
count = 0
while count < len(check_ls):
    a = count[y].find('=')
    if a > count:
        count = a
    y += 1
x = 0
while x < len(check_ls) :
    print(check_ls[x])
    x += 1