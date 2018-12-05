import math
#input
x = float(input("Enter x : "))
#process
if x == 0:
    print("f(%.2f) = %.0f"%(x,x))
elif x < 0:
    ans = math.ceil(math.sqrt(x**2)+1)
    print("f(%.2f) = %.0f" %(x,ans))
elif x>0 and x<=99:
    ans = math.ceil((3*(x**2))-((1-x)**2))
    print("f(%.2f) = %.0f" %(x,ans))
elif x>99:
    ans = math.ceil((2*(math.pow(x,3))) - (x/(math.sqrt(x+1)))) 
    print("f(%.2f) = %.0f" %(x,ans))