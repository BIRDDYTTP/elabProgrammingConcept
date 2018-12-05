print("Upper left corner coordinate:")
x = int(input("  << x axis: "))
y = int(input("  << y axis: "))
ea = int(input("  << Eastern: "))
so = int(input("  << Southern: "))
x_ea = x + ea
y_so = y - so
print("Enter a coordinate:")
x2 = int(input("  << x axis: "))
y2 = int(input("  << y axis: "))
if x<=x2<=x_ea and y_so<=y2<=y:
    print(">>> (%.2f, %.2f) is inside the rectangle." %(x2,y2))
elif x2<x or x2>x_ea or y2<y_so or y2>y:
    print(">>> (%.2f, %.2f) is not inside the rectangle." %(x2,y2))