num = int(input("Enter n : "))
count = 1
while count<2*num:
    if count <= num:
        print('*'*count)
        count += 1
    else:
        print('*'*(num*2-count))
        count += 1