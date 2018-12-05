choice = input("Enter your buffet choice: ")
a = "Korean"
b = "Japanese"
c = "yes"
d = "no"
if choice != a and choice != b:
    print("Sorry, there is no %s buffet." %(choice))    
else:
    day = input("Is today Wednesday (yes/no)? ")
    if choice == a and day == c:
        price = 1500*0.85
        print("Your payment is %.2f Baht." %(price))
    elif choice == a and day == d:
        price = 1500    
        print("Your payment is %.2f Baht." %(price))
    elif choice == b and day == c :
        price = 1000 * 0.85
        print("Your payment is %.2f Baht." %(price))
    elif choice == b and day == d:
        price = 1000
        print("Your payment is %.2f Baht." %(price))