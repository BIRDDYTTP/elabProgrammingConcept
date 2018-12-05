year = int(input("Enter year: "))
if year <=0 :
	print("Invalid year.")
else:
	a = year % 4
	b = year % 100
	c = year % 400
	if a == 0 and b == 0 and c != 0:
		print("%d is not a leap year." %(year))
	elif a == 0 and b != 0 :
		print("%d is a leap year." %(year))
	elif c == 0:
		print("%d is a leap year." %(year))
	else:
		print("%d is not a leap year." %(year))