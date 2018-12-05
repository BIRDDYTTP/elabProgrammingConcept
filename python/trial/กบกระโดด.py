depth = int(input("Enter the depth of the well : "))
jump = int(input("Enter the height the frog can jump : "))
slip = int(input("Enter the height the frog slips down : "))
day = 1
if jump == slip:
    print("The frog will never escape from the well.")
else:    
    while depth > jump :
        leaps = depth - jump
        print("On day %d the frog leaps to the depth of %d meters." %(day,leaps))
        depth = leaps + slip
        print("At night he slips down to the depth of %d meters." %depth)
        day += 1    
    print("The frog can escape the well on day %d." %day)