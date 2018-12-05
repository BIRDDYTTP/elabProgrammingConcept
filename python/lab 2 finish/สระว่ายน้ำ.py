# input
width = float(input("Enter width: "))
length = float(input("Enter length: "))
depth = float(input("Enter depth: "))
# process
volume = width*length*depth
time = (volume*15)/60
# output
print("Time to fill a pool is %.2f minutes." %(time))