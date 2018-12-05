tv = int(input("How many TVs? "))
dvd = int(input("How many DVD players? "))
au = int(input("How many Audio Systems? "))
total = (tv*6000)+(dvd*1500)+(au*3000)
payment = total
if tv<0 or dvd<0 or au<0:
    pass
else:
    if total<24000:
        print("Total price is %.2f baht." %(total))
        print("Your payment is %.2f baht. Thank you!"%(payment))
    else:
        payment = total*0.80
        dc = total*0.20
        print("Total price is %.2f baht." %(total))
        print("You've got a discount of %.2f baht." %(dc))
        print("Your payment is %.2f baht. Thank you!"%(payment))        