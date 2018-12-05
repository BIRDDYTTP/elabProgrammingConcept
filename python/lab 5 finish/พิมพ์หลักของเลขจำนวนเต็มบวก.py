num = int(input())
if num <= 0:
    print("ERROR")
else:
    while num > 0 :
        a = num % 10
        print(a)
        num = num // 10