c = int(input())
a = 1
count = 0
if c >= 0:
    while a <= c:
        b = 1
        x = ''
        y = ''
        while b <= c:
            if c**2 == a**2+b**2:
                if a == y and b == x:
                    pass
                else:
                    count +=1   
            b += 1
    
        a += 1
    if count == 1:    
        print(count)
    elif count != 1:
        count = count // 2
        print(count)
else:
    pass