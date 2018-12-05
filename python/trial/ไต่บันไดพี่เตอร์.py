height = int(input("Enter height of stair : "))
head = (height-1)-1
move = 1

while move!=0:
    i = 0
    while i < height :
        if head < 0:
            head = 0;
        if head > height-2 :
            head = height-2
        
        if i == head:
            print("--o--")
        elif i == head+1:
            print("--^--")
        else:
            print("-----")
        
        i+=1
        
    move = int(input("Enter your moves : "))
    head -= move

print("---<Thank you for playing>---")