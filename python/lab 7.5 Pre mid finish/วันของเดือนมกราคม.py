x = int(input())
n = int(input())
if n > 31 or n <= 0 or x<=0 or x>7:
    print("ERROR")
else:
    different_day = n-x
    ans = different_day%7
    if ans == 0:
        print("Sunday")
    elif ans == 1:
        print("Monday")
    elif ans == 2:
        print("Tuesday")
    elif ans == 3:
        print("Wednesday")
    elif ans == 4:
        print("Thursday")
    elif ans == 5:
        print("Friday")
    elif ans == 6:
        print("Saturday")