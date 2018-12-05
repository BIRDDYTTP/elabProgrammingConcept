import math

# input
x = float(input("Enter x: "))

y = float(input("Enter y: "))

z = float(input("Enter z: "))


# process
a1 = (math.pow(x, y))+z

a2 = (math.cos(0))+(math.log(x))

a3 = (math.fabs(x))+(math.fabs(y))

a4 = (math.sqrt((math.pow(x,2))+(math.pow(y,2))+(math.pow(z,2))))

a5 = (math.pow(math.sin(x),2))+(math.pow(math.cos(x),2))

a6 = (math.pow(x+y,1/5))

a7 = (math.pow(math.e,x*math.log(y)))


# output
print("a1 = %.2f" % a1)
print("a2 = %.2f" % a2)
print("a3 = %.2f" % a3)
print("a4 = %.2f" % a4)
print("a5 = %.2f" % a5)
print("a6 = %.2f" % a6)
print("a7 = %.2f" % a7)
