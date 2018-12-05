num = int(input("Enter a number: "))
digit = int(input("Enter a digit: "))
if num <= -1:
    print("Invalid number.")
    if digit <0 or digit > 9:
        print("Invalid digit.")    
else:
    if digit <0 or digit > 9:
        print("Invalid digit.")
    else:
        ans = (str(num)).count(str(digit))
        if ans ==1:
            print("Digit %d occurs %d time." %(digit,ans))
        else:
            print("Digit %d occurs %d times." %(digit,ans))