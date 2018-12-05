w = float(input("Weight (kg): "))
h = float(input("Height (m): "))
bmi = w/(h*h)
print("BMI is %.1f"%(bmi))
if w<=0 or h<=0:
    print("Invalid weight of hieght")
else: 
    if bmi<18.5:
        print("Underweight")
    elif 18.5 <= bmi < 25:
        print("Normal weight")
    elif 25<= bmi < 30:
        print("Overweight")
    elif bmi >= 30:
        print("Obesity")