import math
num = int(input("Enter a number: "))
count = 0
z = 1
if num < 0:
    print("Invalid input, program terminates.")
else:
    while count <= num:
        print("%d! = "%count, end='')
        y = math.factorial(count)
        x = count
        if x == 0:
            print("1", end='')
            print(" = %d"%y)
            count += 1   
        else:
            while x>0:
                if x > 1:
                    print("%d x "%x ,end='')
                    x -= 1
                elif x == 1:
                    print("%d"%x ,end='')
                    x -= 1
            print(" = %d"%y)
            count += 1