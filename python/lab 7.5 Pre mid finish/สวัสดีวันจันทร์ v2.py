day = int(input())
hr = int(input())
minute = int(input())
if day > 7 or day < 1 or hr >23 or hr < 0 or minute <0 or minute >59:
    pass
else:
    time = (minute / 10)+hr
    if time >= 4.01 and time <= 12.00:
        time = 'morning'
    elif time >= 12.01 and time <= 18.00:
        time = 'afternoon'
    elif time >= 18.01 and time <= 22.00:
        time = 'evening'
    else:
        time = 'night'
    if day==1:
        day = 'sunday'
    elif day == 2 :
        day = 'monday'
    elif day == 3 :
        day = 'tuesday'
    elif day == 4:
        day = 'wednesday'
    elif day == 5:
        day = 'thursday'
    elif day == 6:
        day = 'friday'
    elif day == 7:
        day = 'saturday'
    print("good-%s-%s.png"%(time,day))  