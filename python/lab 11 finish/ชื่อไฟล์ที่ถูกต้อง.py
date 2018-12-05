def check1(f):
    c = f[0:15]
    d = f[16:]
    y = d.count('.')
    e = ''
    a = ''
    if y > 0:
        for x in c:
            if (x == '\\' or x == '/' or x == '*' or x == ':' or x == '|' or x == '"' or x == '<' or x == '>' or x == ' '):
                a = a+'_'
            elif  x == '.' and c.count('.') < (file.count('.')-1):
                a = a+'_'
                e = e+x
            else:
                a = a+x
        for z in d:
            if (z == '\\' or z == '/' or z == '*' or z == ':' or z == '|' or z == '"' or z == '<' or z == '>' or z == ' ' or z =='.') and len(e) < 4 and e.count('.')==1 :
                for y in e:
                    if y.lower() in 'abcdefghijklmnopqrstuvwxyz':
                        e = e+'_'
                    else:
                        e = e+''
            elif len(e) == 4:
                break
            else:
                e = e+z
        a = a+e
        
            
    else:
        for x in c:
            if (x == '\\' or x == '/' or x == '*' or x == ':' or x == '|' or x == '"' or x == '<' or x == '>' or x == ' ' or x == '.' ):
                a = a+'_'
            else:
                a = a+x   
    return a
    
file = str(input())
a = ''
c = ''
if len(file) >=15:
    z = check1(file)
    a = a+z
else:
    for x in file:
        if (x == '\\' or x == '/' or x == '*' or x == ':' or x == '|' or x == '"' or x == '<' or x == '>' or x == ' '):
            a = a+'_'
        elif  x == '.' and c.count('.') < (file.count('.')-1):
            a = a+'_'
            c = c+x
        else:
            a = a+x
print(a)