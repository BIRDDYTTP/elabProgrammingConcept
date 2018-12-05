num = 9
count1 = 1
while count1 <= 9:
    count2 = 1
    show = count1
    while count2 <= 9:
        print(show, end='')
        if show >=9:
            show = 0
        count2 += 1
        show += 1 
    print()
    count1 += 1