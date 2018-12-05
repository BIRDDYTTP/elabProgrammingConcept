def check_prime(n):
    a = 1
    count = 0
    while a <= n:
        ans = n % a
        if ans == 0:
            count += 1
            a += 1
        else:
            a += 1
    if count == 2:
        return True
    else:
        return False

n = int(input("Enter number: "))
if check_prime(n):
    print(n,"is a prime number.")
else:
    print(n,"is not a prime number.")    