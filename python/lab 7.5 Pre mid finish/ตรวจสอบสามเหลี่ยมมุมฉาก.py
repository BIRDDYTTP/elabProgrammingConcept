a = int(input())
b = int(input())
c = int(input())
if a>0 and b>0 and c>0:
    if a**2 == b**2+c**2:
        print("True")
    elif b**2 == a**2+c**2:
        print("True")
    elif c**2 == a**2+b**2:
        print("True")
    else:
        print("False")
else:
    print("False")