l = float(input("Enter level pokemon: "))
x = input("Enter level pokeball: ")
d = float(input("Enter distance: "))
#if l>100 or l < 0:
if l>=0 and l<=40 and (x == "h" or x == "H"):
    s = 100 - (l*d*0.01)
    if s<0:
        s=0
elif l>=41 and l<=60 and (x == "h" or x == "H"):
    s = 100 - (l*d*0.01)
    if s<0:
        s=0 

elif l>=61 and (x == "h" or x == "H"):
    s = 100 - (l*d*0.01)
    if s<0:
        s=0 
elif l>=0 and l<=40 and (x == "m" or x == "M"):
    s = 100 - (l*d*0.03)
    if s<0:
        s=0

elif l>=41 and l<=60 and (x == "m" or x == "M"):
    s = 100 - (l*d*0.05)        
    if s<0:
        s=0
elif l>=61  and (x == "m" or x == "M"):
    s = 100 - (l*d*0.08)
    if s<0:
        s=0  
elif l>=0 and l<=40 and (x == "l" or x == "L"):
    s = 100 - (l*d*0.05) 
    if s<0:
        s=0  
elif l>=41 and l<=60 and (x == "l" or x == "L"):
    s = 100 - (l*d*0.03)
    if s<0:
        s=0
elif l>=0  and (x == "l" or x == "L"):
    s = 100 - (l*d*0.1)
    if s<0:
        s=0
print("%.2f percent."%s)