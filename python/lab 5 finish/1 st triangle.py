h = int(input("Enter height: "))
loop = h
space = 3
if(h==1):
    print("1")
    loop = loop-1
if(h==0):
    pass
else:
    while(loop>0):
        if(loop == h):
            print(" "*((loop*2)-2) + "1")
        else:
            print(" "*((loop*2)-2) + "1" + " "*space+"1")
            space = space+4
        loop = loop-1