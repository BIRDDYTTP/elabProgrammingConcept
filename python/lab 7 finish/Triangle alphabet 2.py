num = int(input("Enter a number: "))
x = num 
if num <= 0 or num >26:
        print("Invalid input, program terminates.")
else:
        while x >= 1 :
                y = 1
                while y <= x :
                        print(chr(ord('A')+(1*(y-1))), end="")
                        y += 1 
                print()
                x -= 1