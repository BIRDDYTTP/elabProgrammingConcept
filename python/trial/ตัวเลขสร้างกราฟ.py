index = int(input("Input index : "))
count = 0
ls = []
while count < index: 
    num = int(input("Enter number [%d] : "%count))
    ls.append(num)
    count += 1
count2 = 12
while count2 >= -1:
    count3 = 0
    if count2>=1 and count2 <= 11:
        print("%2d|"%(count2-1),end='')
    elif count2 ==12 or count2 == 0:
        print("   ",end='')
    while count3 <= index-1:
        if count2 == 12 or count2 == 0:
            print("__ ", end='')
            count3 += 1
        elif count2 == -1:
            if count3 == 0:
                print("%4d"%count3,end='')
                count3 += 1
            else:
                print("%3d"%count3,end='')
                count3 += 1
        elif count2 == 1:
            print("  |",end='')
            count3 += 1
        else:
            if 1<=ls[count3] and ls[count3]>=count2-1:
                print("* |",end='')
                count3 += 1
            else:
                print("  |",end='')
                count3 += 1
    count2 -= 1
    print()