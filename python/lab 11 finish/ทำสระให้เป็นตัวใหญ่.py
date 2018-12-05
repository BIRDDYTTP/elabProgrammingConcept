st = str(input())
y = ''
for x in st:
    if x.upper() == 'A' or x.upper() == 'E'or x.upper() == 'I' or x.upper() == 'O' or x.upper() == 'U':
        x = x.upper()
        y = y+x
    else:
        x = x.lower()
        y = y+x
print(y)