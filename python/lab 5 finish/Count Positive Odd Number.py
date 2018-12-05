count = 0
while True:
    num = int(input("Enter number: "))
    if num < 0 :
        break
    else:
        if num % 2 != 0 :
            count = count+1
            continue
        else:
            continue
print("Received %d odd numbers"%count)