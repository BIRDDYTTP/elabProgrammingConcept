num = int(input("Enter positive integer: "))
if num <= 0:
    print("Invalid number.")
else:
    while num > 1:
        count = 2
        while count <= num:
            if num % count == 0:
                print(count)
                num = num // count
                continue
            else:
                count += 1