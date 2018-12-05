minute = int(input("Minutes before due: "))
temp = float(input("Temperature: "))
rain = input("Is it raining (y/n)? ")
day = (minute/(60*24))
day2 = (minute//(60*24))
if rain == 'Y' or rain == 'y' or rain == 'N' or rain =='n':     
    if day-day2 >= 0.5:
        day3 = day2+1
    else:
        day3 = day2
        
    print(">>> %d days before due."%day3)
    if day3 < 2:
        print(">>> I will do the assignment.")
    elif day3 > 5:
        print(">>> I will not do the assignment.")
    elif (day3 <= 5 and day3 >= 2)and(temp>40 or (temp>25 and (rain == 'Y'or rain == 'y'))):
        print(">>> I will not do the assignment.")
    elif (day3 <= 5 and day3 >= 2)and(temp>40 or (temp>25 and (rain == 'N'or rain == 'n'))):
        print(">>> I will do the assignment.")
    else:     
        print(">>> I will do the assignment.")  