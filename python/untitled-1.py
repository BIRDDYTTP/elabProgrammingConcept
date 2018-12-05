num = int(input())
count = 0
while count < num:
    count2 = 0
    while count2 < num:
        if (count == 0 or count == num-1):
            print("* ", end="")
        else:
            if count2 == 0 or count2 == num-1:
                print("* ", end="")
            else:
                print("  ", end="")
        count2+=1
    print()
    count+=1