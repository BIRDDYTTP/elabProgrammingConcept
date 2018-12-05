while True:
    print("<<Point a>>")
    xa = int(input("Enter x coordinate: "))
    ya = int(input("Enter y coordinate: "))
    print("<<Point b>>")
    xb = int(input("Enter x coordinate: "))
    yb = int(input("Enter y coordinate: "))
    if xa == 0 and ya == 0 and xb == 0 and yb == 0:
        print("Goodbye")
        break
    else:
        distance = ((xa-xb)**2 + (ya-yb)**2)**0.5
        print("Distance between (%d, %d) and (%d, %d):" %(xa,ya,xb,yb))
        print("Euclidean distance is %.2f." %distance)
        hor = abs(xa-xb)
        ver = abs(ya-yb)
        print("Horizontal distance is %d." %hor)
        print("Vertical distance is %d." %ver)
        if xa-xb==0 and ya-yb == 0:
            print("We are going nowhere.")
        elif xa-xb>0 and ya-yb == 0:
            print("We are going west.")
        elif xa-xb<0 and ya-yb==0:
            print("We are going east.")
        elif xa-xb==0 and ya-yb>0:
            print("We are going south.")
        elif xa-xb==0 and ya-yb<0:
            print("We are going north.")
        elif xa-xb>0 and ya-yb>0:
            print("We are going south-west.")
        elif xa-xb<0 and ya-yb<0:
            print("We are going north-east.")
        elif xa-xb>0 and ya-yb<0:
            print("We are going north-west.")
        elif xa-xb<0 and ya-yb>0:
            print("We are going south-east.")
        continue