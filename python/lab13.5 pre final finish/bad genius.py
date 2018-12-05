ordinary = str(input())
code = str(input())
password = str(input())
ordinary = ordinary.replace(' ','')
ch_ls1 = []
ch_ls2 = []
for x in ordinary:
    if x not in ch_ls1:
        ch_ls1.append(x)
for x in code:
    ch_ls2.append(x)
for x in password:
    if x in ch_ls2:
        a = ch_ls2.index(x)
        print(ch_ls1[a], end='')
    else:
        print(x,end='')