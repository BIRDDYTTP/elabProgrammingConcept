# input and process
exerciseI = int(input("Enter your exercise time 1: "))
exerciseII = int(input("Enter your exercise time 2: "))
sum = exerciseI+exerciseII
hours = sum//3600
minutes = (sum%3600)//60
seconds = (sum%3600)%60
# output
print("It is", hours, "hours", minutes, "minutes and", seconds, "seconds.")