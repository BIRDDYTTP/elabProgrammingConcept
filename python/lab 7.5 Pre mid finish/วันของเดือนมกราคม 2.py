day_week = input()
day = int(input())
sun = 'Sunday'
mon = 'Monday'
tue = 'Tuesday'
wed = 'Wednesday'
thu = 'Thursday'
fri = 'Friday'
sat = 'Saturday'
if day >31 or day < 1:
    print("ERROR")
else:
    if day_week == sun:
        dif_day = day - 1
        ans = dif_day % 7
        if ans == 0:
            print(sun)
        elif ans == 1:
            print(mon)
        elif ans == 2:
            print(tue)
        elif ans == 3:
            print(wed)
        elif ans == 4:
            print(thu)
        elif ans == 5:
            print(fri)
        elif ans == 6:
            print(sat)
    elif day_week == mon :
        dif_day = day - 1
        ans = dif_day % 7
        if ans == 0:
            print(mon)
        elif ans == 1:
            print(tue)
        elif ans == 2:
            print(wed)
        elif ans == 3:
            print(thu)
        elif ans == 4:
            print(fri)
        elif ans == 5:
            print(sat)
        elif ans == 6:
            print(sun)
    elif day_week == tue:
        dif_day = day - 1
        ans = dif_day % 7
        if ans == 0:
            print(tue)
        elif ans == 1:
            print(wed)
        elif ans == 2:
            print(thu)
        elif ans == 3:
            print(fri)
        elif ans == 4:
            print(sat)
        elif ans == 5:
            print(sun)
        elif ans == 6:
            print(mon)        
    elif day_week == wed:
        dif_day = day - 1
        ans = dif_day % 7
        if ans == 0:
            print(wed)
        elif ans == 1:
            print(thu)
        elif ans == 2:
            print(fri)
        elif ans == 3:
            print(sat)
        elif ans == 4:
            print(sun)
        elif ans == 5:
            print(mon)
        elif ans == 6:
            print(tue)
    elif day_week == thu:
        dif_day = day - 1
        ans = dif_day % 7
        if ans == 0:
            print(thu)
        elif ans == 1:
            print(fri)
        elif ans == 2:
            print(sat)
        elif ans == 3:
            print(sun)
        elif ans == 4:
            print(mon)
        elif ans == 5:
            print(tue)
        elif ans == 6:
            print(wed)
    elif day_week == fri:
        dif_day = day - 1
        ans = dif_day % 7
        if ans == 0:
            print(fri)
        elif ans == 1:
            print(sat)
        elif ans == 2:
            print(sun)
        elif ans == 3:
            print(mon)
        elif ans == 4:
            print(tue)
        elif ans == 5:
            print(wed)
        elif ans == 6:
            print(thu)
    elif day_week == sat:
        dif_day = day - 1
        ans = dif_day % 7
        if ans == 0:
            print(sat)
        elif ans == 1:
            print(sun)
        elif ans == 2:
            print(mon)
        elif ans == 3:
            print(tue)
        elif ans == 4:
            print(wed)
        elif ans == 5:
            print(thu)
        elif ans == 6:
            print(fri)           
    else:
        print('ERROR')