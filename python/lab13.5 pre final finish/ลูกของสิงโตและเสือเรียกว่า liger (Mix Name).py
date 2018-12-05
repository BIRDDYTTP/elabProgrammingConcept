ani1 = str(input())
ani2 = str(input())
a = ''
b = ''
count = 0
for x in ani1:
    if x in 'aeiou':
        count += 1
    if count > 1:
        break
    else:
        a += x
if ani2.count('a')+ani2.count('e')+ani2.count('i')+ani2.count('o')+ani2.count('u') == 0:
    a += ani2
else:
    for x in ani2:
        if 'a' in b  or 'i' in b  or 'o' in b  or 'e' in b  or 'u'  in b:
            a += x
        else:
            b += x
print(a)