import math

# input
h = int(input('Enter number of hours: '))
m = int(input('Enter number of minutes: '))

# process and output
if m<0 or m>59 or h<0:
    print("Input Error!")
else:
    time = (h*60)+m
    if time <= 15:
        print("No charge, thanks.")
    elif time > 15 and time <= 120:
        print("Total amount due is 10 Bahts.")
    else:
        b = math.ceil((time-120)/60)
        c = (b*10)+10
        print("Total amount due is %d Bahts." %(c))    