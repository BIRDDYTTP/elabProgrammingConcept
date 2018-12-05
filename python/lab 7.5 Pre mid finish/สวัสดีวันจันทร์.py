day = int(input())
hr = int(input())
minute = int(input())
minute2 = minute/100
time = hr+minute2
if day >7 or day < 1 or hr < 0 or hr >23 or minute < 0 or minute > 59:
    pass
elif day == 1:
    if time >= 4.01 and time <= 12.00:
        print("good-morning-sunday.png")
    elif time >= 12.01 and time <= 18.00:
        print("good-afternoon-sunday.png")
    elif time >= 18.01 and time <= 22.00:
        print("good-evening-sunday.png")
    else:
        print("good-night-sunday.png")
elif day == 2:
    if time >= 4.01 and time <= 12.00:
        print("good-morning-monday.png")
    elif time >= 12.01 and time <= 18.00:
        print("good-afternoon-monday.png")
    elif time >= 18.01 and time <= 22.00:
        print("good-evening-monday.png")
    else:
        print("good-night-monday.png")
elif day == 3:
    if time >= 4.01 and time <= 12.00:
        print("good-morning-tuesday.png")
    elif time >= 12.01 and time <= 18.00:
        print("good-afternoon-tuesday.png")
    elif time >= 18.01 and time <= 22.00:
        print("good-evening-tuesday.png")
    else:
        print("good-night-tuesday.png")
elif day == 4:
    if time >= 4.01 and time <= 12.00:
        print("good-morning-wednesday.png")
    elif time >= 12.01 and time <= 18.00:
        print("good-afternoon-wednesday.png")
    elif time >= 18.01 and time <= 22.00:
        print("good-evening-wednesday.png")
    else:
        print("good-night-wednesday.png")
elif day == 5:
    if time >= 4.01 and time <= 12.00:
        print("good-morning-thursday.png")
    elif time >= 12.01 and time <= 18.00:
        print("good-afternoon-thursday.png")
    elif time >= 18.01 and time <= 22.00:
        print("good-evening-thursday.png")
    else:
        print("good-night-thursday.png")
elif day == 6:
    if time >= 4.01 and time <= 12.00:
        print("good-morning-friday.png")
    elif time >= 12.01 and time <= 18.00:
        print("good-afternoon-friday.png")
    elif time >= 18.01 and time <= 22.00:
        print("good-evening-friday.png")
    else:
        print("good-night-friday.png")
elif day == 7:
    if time >= 4.01 and time <= 12.00:
        print("good-morning-saturday.png")
    elif time >= 12.01 and time <= 18.00:
        print("good-afternoon-saturday.png")
    elif time >= 18.01 and time <= 22.00:
        print("good-evening-saturday.png")
    else:
        print("good-night-saturday.png")