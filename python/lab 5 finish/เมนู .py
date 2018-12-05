print("---<< Main Menu >>---\n    <B>urger Meal\n    <C>hicken Meal\n    <P>asta Meal")
a = input("Enter your choice: ")
if a == 'B' or a == 'b':
    print("---<< Burger Sub Menu >>---\n    <R>egular Burger\n    <C>heese Burger\n    <D>ouble Cheese Burger")
    b = input("Enter your choice: ")
    if b == 'R' or b == 'r' :
        print("Your Regular Burger is 60 Baht.")
    elif b == 'C'  or b == 'c' :
        print("Your Cheese Burger is 75 Baht.")
    elif b == 'D' or b == 'd':
        print("Your Double Cheese Burger is 90 Baht.")
    else:
        print("Invalid sub menu choice.")        
elif a == 'C' or a == 'c':
    print("---<< Chicken Sub Menu >>---\n    <F>ried Chicken\n    <G>rilled Chicken\n    <C>hef's Chicken")
    b = input("Enter your choice: ")
    if b == 'F'or b == 'f' :
        print("Your Fried Chicken is 120 Baht.")
    elif b == 'G'  or b == 'g':
        print("Your Grilled Chicken is 150 Baht.")
    elif b == 'C' or b == 'c':
        print("Your Chef's Chicken is 180 Baht.")
    else:
        print("Invalid sub menu choice.")        
elif a == 'P' or a == 'p':
    print("---<< Pasta Sub Menu >>---\n    <S>paghetti de Italiano\n    <L>asagna Supreme\n    <M>acaroni Special")
    b = input("Enter your choice: ")
    if b == 'S' or b == 's' :
        print("Your Spaghetti de Italiano is 90 Baht.")
    elif b == 'L' or b == 'l': 
        print("Your Lasagna Supreme is 120 Baht.")
    elif b == 'M' or b == 'm' :
        print("Your Macaroni Special is 100 Baht.") 
    else:
        print("Invalid sub menu choice.")        
else:
    print("Invalid main menu choice.")