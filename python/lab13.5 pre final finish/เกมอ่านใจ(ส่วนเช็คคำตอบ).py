hind = str(input())
seek = str(input())
checkls = []
indexls = []
position = 0
HaveIn = 0
hind2 = ''
seek2 = ''
for i in range(len(hind)):
    indexls.append(i)
for x in range(len(hind)):
    if hind[x] == seek[x]:
        checkls.append(x)
        position += 1
for i in range(len(hind)):
    if not i in checkls:
        hind2 += hind[i]
        seek2 += seek[i]
for x in seek2:
    if x in hind2:
        HaveIn += 1
        hind2 = hind2.replace(x,'',1)
        seek2 = seek2.replace(x,'',1)
print('%d-%d' %(position,HaveIn))