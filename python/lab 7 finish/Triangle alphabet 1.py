num = int(input("Enter a number: "))
count = 0
b = ''
if num <= 0 or num >26:
        print("Invalid input, program terminates.")
else:
        while count+1 <= num :
                b = b+chr(ord('A')+(1*count))
                print(b)
                count=count+1