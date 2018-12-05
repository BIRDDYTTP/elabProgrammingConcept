num = int(input())
Sum=0
count=0
avg=0
while num>0 :
    grade = float(input())
    if grade>=0 :
        Sum+=grade
        if grade>40 :
            count+=1
if count>0 :
    avg=Sum/num
    print("%.2f %2f"% avg, count)
elif count==0 :
    print("%.2f %2f"% 0, count)