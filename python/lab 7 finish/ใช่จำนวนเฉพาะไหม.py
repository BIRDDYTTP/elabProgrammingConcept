count = 0
x = 1
while True:
    num = int(input("Enter a number: "))
    if num <= 1 and num != 0 :
        print("Invalid input, try again.")
        continue
    elif num == 0 :
        print("End of program, goodbye.")
        break
    else:
        while x <= num:
            ans = num%x
            if ans == 0:
                count += 1
                x += 1
                continue
            else:
                x += 1
                continue
        if count == 2 :
            print("%d is a prime number." %num)
            x = x-(x-1)
            count = count-(count)
            continue
        elif count != 2:
            print("%d is not a prime number." %num)
            x = x-(x-1)
            count = count-(count)
            continue