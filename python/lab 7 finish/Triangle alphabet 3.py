num = int(input("Enter a number: "))
x = num*2 
count = 0
a = ''
if num <= 0 or num >26:
        print("Invalid input, program terminates.")
else:
        while x >= 1 :
                if count+1 <= num:
                        a = a + chr(ord('A')+(1*count))
                        print(a)
                        count = count+1
                        x -= 1
                else:
                        y = 2
                        while y <= x :
                                print(chr(ord('A')+(1*(y-2))), end="")
                                y += 1 
                        print()
                        x -= 1