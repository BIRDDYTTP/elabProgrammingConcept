h = int(input("Enter height: "))
w = int(input("Enter width: "))
count = 1
if h<=0 or w <= 0:
    print("Invalid input, program terminates.")
else:
    while count <= h:
        if count % 2 == 1 :
            a ='* '*w
            print(a)
            count += 1
        else:
            a = ' '+('* '*w) 
            print(a)
            count += 1