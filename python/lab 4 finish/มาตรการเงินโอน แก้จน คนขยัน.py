age = int(input("Enter your age: "))
income = int(input("Enter your net income: "))
if age<15 or age>60:
	print("Invalid age.")
elif income < 0 or income >79999:
	print("Invalid income.")
else:
	if income<=30000:
		ic_tax = income*0.2
		print("Your negative income tax is %.2f Baht." %(ic_tax))
	elif income>30000 and income<=79999:
		ic_tax = (30000*0.2)-((income-30000)*0.12)
		print("Your negative income tax is %.2f Baht." %(ic_tax))