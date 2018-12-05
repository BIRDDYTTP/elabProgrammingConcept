target = 72

#input
number = int(input("Enter your guess (0 - 100): "))

# process and output
if number>100 or number < 0:
    print("Sorry, out of range, try again later.")
elif number < target:
    print("Sorry, your guess is too low, try again later.")
elif number > target :
    print("Sorry, your guess is too high, try again later.")
else:
    print("Congratulations, your guess is correct.")