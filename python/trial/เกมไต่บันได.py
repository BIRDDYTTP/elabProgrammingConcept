num = int(input("Enter height of stair : "))
count = 1

while count<=num:
    count2 = 1
    while count2 <=5:
        if count == num-1 and count2 == 3:
            print("o", end='')
            count2 += 1
        elif count == num and count2 == 3:
            print("^", end='')
            count2 += 1
        else:
            print("-", end='')
            count2 +=1
    count += 1
    print()
leg = num
head = num-1
while True:
    move = int(input("Enter your move : "))
    count3 = 1
    leg -= move
    head -= move
    if leg <= 1 and head <= 1:
        leg = 2
        head = 1
    elif leg>=num and head >= num:
        leg = num
        head = num-1
    if move == 0 :
        print("---<Thank you for playing>---")
        break
    else:
        while count3 <= num:
            count4 = 1
            while count4 <= 5:
                if count3 == leg and count4 == 3:
                    print("^", end='')
                    count4 += 1
                elif count3 == head and count4 == 3:
                    print("o", end='')
                    count4 += 1
                else:
                    print("-", end='')
                    count4 += 1
            count3+=1
            print()
        continue