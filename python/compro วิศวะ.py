x = float(input("Enter your homework percent: "))
y = float(input("Enter your midterm percent: "))
z = float(input("Enter your final percent: "))
score = (x*0.1)+(y*0.4)+(z*0.5)/1
print(f"Your total score is {score:.2f}.")
if score >= 80:
    print("Your grade is A.")

elif score >= 75 and score < 80:
    print("Your grade is B+.")
    
elif score >= 70 and score < 75:
    print("Your grade is B.")
        
elif score >= 65 and score <70:
    print("Your grade is C+.")
    
elif score >= 60 and score < 65:
    print("Your grade is C.")
        
elif score >= 55 and score <60:
    print("Your grade is D+.")
            
elif score >= 50 and score <55:
    print("Your grade is D.")
                
elif score < 50:
    print("Your grade is F.")