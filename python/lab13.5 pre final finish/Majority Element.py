num = int(input())
lsA = []
for x in range(num):
    st = str(input())
    lsA.append(st)
checkls = []
for x in lsA:
    if ord(x) in checkls:
        pass
    else:
        checkls.append(ord(x))
countchc = []
char = []
for x in checkls:
    count = lsA.count(chr(x))
    countchc.append(count)
    char.append(chr(x))
printls = []
count = 0
while count <= len(countchc)-1:
    if countchc[count] >= (num//2)+1:
        printls.append(char[count])
    count += 1
if len(printls) == 0:
    print(len(printls))
else:
    for x in printls:
        print(x)