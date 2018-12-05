target = 72
count = 0
while True:
    a = int(input("Enter your guess: "))
    if a<0 or a >100:
        print("Sorry, your guess is out of range.")
        count = count+1
        continue
    elif a < target and a>=0 and a<=100:
        print("Sorry, your guess is too low.")
        count = count+1
        continue
    elif a > target and a>=0 and a<=100:
        print("Sorry, your guess is too high.")
        count = count+1
        continue
    elif a == target:
        print("Congratulations, your guess is correct.")
        count = count+1
        break
print("Total number of guesses is %d."%count)