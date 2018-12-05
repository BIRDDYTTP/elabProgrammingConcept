num = input("Enter a number (just [Enter] to quit): ")
x = num
y = num
count = 0
z = num
if num == '':
    print("Nothing to do.")
else:
    while num != '':
        num2 = input("Enter a number (just [Enter] to quit): ")
        if num2 > num:
            x = num2
            count += 1
            z += num2
        elif num2 < num:
            y = num2
            count += 1
            z += num2
        elif num2 == '':
            num = ''
            break
    ave = z/count
    print("The maximum is ",x)
    print("The minimum is ",y)
    print("The average is ",ave)
    